import socket
import ssl

from building_web_browser_from_scratch.core.models.ports.dto_request import ResponseLine
from building_web_browser_from_scratch.core.ports import RequestPort

from building_web_browser_from_scratch.core.models import (
    Request, 
    RequestLine, 
    BaseHeader, 
    Response,
    Destiny
)

from building_web_browser_from_scratch.adapters.conversors import (
    ConvertRequestToStr, 
    ConvertStrToRequest
)

class SocketHTTPSRequest(RequestPort):
    
    def get_socket(self, to: Destiny) -> socket.socket:
        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP
        )
        s.connect((to.hostname, to.port))
        hostname = to.hostname
        
        # wrapping the socket to use https
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(s, server_hostname=hostname)
        return s

    def _get_encoded_request(self, input: Request) -> str:
        request_as_str = ConvertRequestToStr().run(input)
        encoded_request = request_as_str.encode('utf8')
        return encoded_request

    def _get_response(self, s: socket.socket) -> Response:
        response = s.makefile("r", encoding="utf8", newline="\r\n")
        
        statusline = response.readline()
        split_by_space = statusline.split(" ", 2)

        if len(split_by_space) != 3:
            raise ValueError(f"invalid statusline. expected three elements but got: {split_by_space}")

        version, status, explanation = split_by_space

        try:
            status = int(status)
        except ValueError as e:
            raise ValueError(f"invalid value for status: {status}")

        response_headers = []
        while True:
            line = response.readline()
            if line == "\r\n": break
            name, value = line.split(":", 1)
            response_headers.append(
                BaseHeader(
                    name=name,
                    value=value,
                )
            )

        content = response.readline()
        
        return Response(
            response_line=ResponseLine(
                version=version,
                status=status,
                explanation=explanation
            ),
            headers=response_headers,
            content=content
        )

    def _send_request(self, input: Request, to: Destiny):
        if not isinstance(input, Request):
            raise TypeError('input must be a Request')
        if not isinstance(to, Destiny):
            raise TypeError('to must be a Destiny')

        s = self.get_socket(to)
        encoded_request = self._get_encoded_request(input)
        s.send(encoded_request)
        response = self._get_response(s)
        s.close()
        return response

    

        






        

        

        

        
    
    