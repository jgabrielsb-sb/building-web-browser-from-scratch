from building_web_browser_from_scratch.core.ports import ConversorPort
from building_web_browser_from_scratch.core.models import (
    Request, 
    RequestLine, 
    MethodEnum, 
    BaseHeader
)

class ConvertStrToRequest(ConversorPort):
    def get_request_line(self, input: str) -> RequestLine:
        
        if not isinstance(input, str):
            raise TypeError('input must be a str')

        # getting each item of the request line
        split_by_space = input.split(" ")
        if not len(split_by_space) == 3:
            raise ValueError(f'the request_line should have three elements: the method, the path and the http version splitted by spaces, but got: {split_by_space}')
        
        # getting the method of the request line
        method = split_by_space[0]
        try:
            method = MethodEnum(method)
        except ValueError as e:
            raise ValueError(f'error while converting the value {method} to a method: {e}')

        # getting the path and the http version of the request line
        path, http_version = split_by_space[1:]

        request_line = RequestLine(
            method=method,
            http_version=http_version,
            path=path,
        )

        return request_line

    def get_header(self, input: str) -> BaseHeader:
        if not isinstance(input, str):
            raise TypeError('input must be a str')

        split_by_colon = input.split(":")
        if not len(split_by_colon) == 2:
            raise ValueError(f'the header should have two elements: the name and the value splitted by a colon, but got: {split_by_colon}')

        split_by_colon = [var.removeprefix(" ") for var in split_by_colon]
        name, value = split_by_colon
        return BaseHeader(name=name, value=value)

    def has_content(self, lines: list[str]):
        if lines[-1] == "":
            return False
        
        return True

        

    def _run(self, input: str) -> Request:
        if not isinstance(input, str):
            raise TypeError('input must be a str')

        lines = input.split("\r\n")
        request_has_content = self.has_content(lines)
        
        # removing empty lines
        lines = [line for line in lines if line != ""]

        request_line = self.get_request_line(lines[0])
        headers = [self.get_header(line) for line in lines[1:-1]]
        content = lines[-1] if request_has_content else None

        return Request(
            request_line=request_line, 
            headers=headers, 
            content=content
        )

        



       
        
       
        

        




        #return Request(request_line=request_line, headers=headers)