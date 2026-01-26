
import pytest

from building_web_browser_from_scratch.adapters.conversors import ConvertStrToRequest
from building_web_browser_from_scratch.core.models import Request, RequestLine, BaseHeader, MethodEnum

class TestGetRequestLine:
    def test_if_raises_type_error_when_input_is_not_a_str(self):
        convert_str_to_request = ConvertStrToRequest()
        with pytest.raises(TypeError) as e:
            convert_str_to_request.get_request_line(None)
        assert "input must be a str" in str(e.value)

    def test_if_returns_the_correct_request_line(self):
        convert_str_to_request = ConvertStrToRequest()
        request_line = convert_str_to_request.get_request_line("GET / HTTP/1.0")
        assert isinstance(request_line, RequestLine)
        assert request_line.method == MethodEnum.GET
        assert request_line.path == "/"
        assert request_line.http_version == "HTTP/1.0"

    def test_if_raises_value_error_when_the_request_line_is_not_valid(self):
        convert_str_to_request = ConvertStrToRequest()
        with pytest.raises(ValueError) as e:
            convert_str_to_request.get_request_line("GET / HTTP/1.0 1.0")
        assert "the request_line should have three elements: the method, the path and the http version splitted by spaces, but got: ['GET', '/', 'HTTP/1.0', '1.0']" in str(e.value)

    def test_if_raises_value_error_when_the_method_is_not_valid(self):
        convert_str_to_request = ConvertStrToRequest()
        with pytest.raises(ValueError) as e:
            convert_str_to_request.get_request_line("GETT / HTTP/1.0")
        assert "error while converting the value GETT to a method" in str(e.value)
        assert "'GETT' is not a valid MethodEnum" in str(e.value)

class TestGetHeader:
    def test_if_raises_type_error_when_input_is_not_a_str(self):
        convert_str_to_request = ConvertStrToRequest()
        with pytest.raises(TypeError) as e:
            convert_str_to_request.get_header(None)
        assert "input must be a str" in str(e.value)

    def test_if_raises_value_error_when_the_header_is_not_valid(self):
        convert_str_to_request = ConvertStrToRequest()
        with pytest.raises(ValueError) as e:
            convert_str_to_request.get_header("Host localhost")
       
        assert "the header should have two elements" in str(e.value)

    def test_if_returns_the_correct_header(self):
        convert_str_to_request = ConvertStrToRequest()
        header = convert_str_to_request.get_header("Host: localhost")
        assert isinstance(header, BaseHeader)
        assert header.name == "Host"
        assert header.value == "localhost"

    

class TestConvertStrToRequest:
    def test_if_raises_type_error_when_input_is_not_a_str(self):
        convert_str_to_request = ConvertStrToRequest()
        with pytest.raises(TypeError) as e:
            convert_str_to_request._run(None)
        assert "input must be a str" in str(e.value)

    def test_sucess_case_1(self):
        request_str = "GET / HTTP/1.0\r\n"
        request_str += "\r\n"

        request = ConvertStrToRequest()._run(request_str)
        assert isinstance(request, Request)
        assert request.request_line.method == MethodEnum.GET
        assert request.request_line.path == "/"
        assert request.request_line.http_version == "HTTP/1.0"
        assert request.headers == []
        assert request.content is None

    def test_sucess_case_2(self):
        request_str = "GET / HTTP/1.0\r\n"
        request_str += "Host: localhost\r\n"
        request_str += "\r\n"
        request_str += "Hello, world!"

        request = ConvertStrToRequest()._run(request_str)
        assert isinstance(request, Request)
        assert request.request_line.method == MethodEnum.GET
        assert request.request_line.path == "/"
        assert request.request_line.http_version == "HTTP/1.0"
        assert request.headers == [BaseHeader(name="Host", value="localhost")]
        assert request.content == "Hello, world!"

    def test_sucess_case_3(self):
        request_str = "GET / HTTP/1.0\r\n"
        request_str += "Host: localhost\r\n"
        request_str += "Content-Length: 13\r\n"
        request_str += "\r\n"
        request_str += "Hello, world!"

        request = ConvertStrToRequest()._run(request_str)
        assert isinstance(request, Request)
        assert request.request_line.method == MethodEnum.GET
        assert request.request_line.path == "/"
        assert request.request_line.http_version == "HTTP/1.0"
        assert request.headers == [BaseHeader(name="Host", value="localhost"), BaseHeader(name="Content-Length", value="13")]
        assert request.content == "Hello, world!"

    
    

