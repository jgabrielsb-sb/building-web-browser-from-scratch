import pytest

from building_web_browser_from_scratch.adapters.conversors import ConvertRequestToStr
from building_web_browser_from_scratch.core.models import (
    RequestLine, 
    MethodEnum, 
    BaseHeader,
    Request
)

class TestFormatRequestLine:
    def test_if_raises_type_error_when_input_is_not_a_request_line(self):
        convert_request_to_str = ConvertRequestToStr()
        with pytest.raises(TypeError) as e:
            convert_request_to_str.format_request_line(None)
        assert "request_line must be RequestLine" in str(e.value)

    def test_if_returns_the_correct_request_line(self):
        convert_request_to_str = ConvertRequestToStr()
        request_line = RequestLine(
            method=MethodEnum.GET,
            path="/",
            http_version="HTTP/1.0"
        )
        assert convert_request_to_str.format_request_line(request_line) == "GET / HTTP/1.0\r\n"

class TestFormatHeader:
    def test_if_raises_type_error_when_input_is_not_a_base_header(self):
        convert_request_to_str = ConvertRequestToStr()
        with pytest.raises(TypeError) as e:
            convert_request_to_str.format_header(None)
        assert "header must be a BaseHeader" in str(e.value)

    def test_if_returns_the_correct_header(self):
        convert_request_to_str = ConvertRequestToStr()
        header = BaseHeader(name="Host", value="localhost")
        assert convert_request_to_str.format_header(header) == "Host: localhost\r\n"

class TestRun:
    def test_if_raises_type_error_when_input_is_not_a_request(self):
        convert_request_to_str = ConvertRequestToStr()
        with pytest.raises(TypeError) as e:
            convert_request_to_str._run(None)
        assert "input must be Request" in str(e.value)

    def test_if_returns_the_correct_request(self):
        convert_request_to_str = ConvertRequestToStr()
        request = Request(
            request_line=RequestLine(
                method=MethodEnum.GET, 
                path="/", 
                http_version="HTTP/1.0"), 
            headers=[
                BaseHeader(name="Host", value="localhost"),
                BaseHeader(name="User-Agent", value="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
            ]
        )
        assert convert_request_to_str.run(request) == "GET / HTTP/1.0\r\nHost: localhost\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\r\n\r\n"