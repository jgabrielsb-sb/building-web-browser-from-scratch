import socket

from building_web_browser_from_scratch.adapters.conversors import ConvertRequestToStr
from building_web_browser_from_scratch.core.models import (
    Request, 
    RequestLine, 
    MethodEnum, 
    BaseHeader
)

if __name__ == "__main__":
    ## getting request as tr
    request = Request(
        request_line=RequestLine(method=MethodEnum.GET, path="/", http_version="HTTP/1.0"),
        headers=[BaseHeader(name="Host", value="localhost")]
    )
    convert_request_to_str = ConvertRequestToStr()
    request_str = convert_request_to_str.run(request)
    

    ## sending via socket
    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP
    )
    s.connect(('example.org', 80))
    s.send(request_str.encode('utf8'))

    ## getting response
    response = s.makefile("r", encoding="utf8", newline="\r\n")
    
    while True:
        line = response.readline()
        print(line)

        if line == '\r\n': break

