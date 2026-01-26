from building_web_browser_from_scratch.core.ports import ConversorPort
from building_web_browser_from_scratch.core.models import (
    Request, 
    RequestLine, 
    BaseHeader
)

class ConvertRequestToStr(ConversorPort):

    def format_request_line(self, request_line: RequestLine) -> str:

        if not isinstance(request_line, RequestLine):
            raise TypeError(f'request_line must be RequestLine')

        return f"{request_line.method.value} {request_line.path} {request_line.http_version}\r\n"

    def format_header(self, header: BaseHeader) -> str:
        if not isinstance(header, BaseHeader):
            raise TypeError('header must be a BaseHeader')

        return f"{header.name}: {header.value}\r\n"
    
    def _run(self, input: Request):
        if not isinstance(input, Request):
            raise TypeError(f'input must be Request')

        result = self.format_request_line(input.request_line)

        for header in input.headers:
            result += self.format_header(header)

        result += "\r\n"
        return result


        
