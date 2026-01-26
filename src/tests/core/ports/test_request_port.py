from building_web_browser_from_scratch.core.ports import RequestPort
from building_web_browser_from_scratch.core.models import Request, RequestLine, BaseHeader, MethodEnum
import pytest

@pytest.fixture
def request_port():
    class RequestPortImpl(RequestPort):
        def _get(self, input: Request):
            return "test"
    return RequestPortImpl()

class TestRequestPort:
    def test_if_raises_type_error_when_input_is_not_a_get_input(self, request_port: RequestPort):
        with pytest.raises(TypeError) as e:
            request_port.get(None)
        assert "input must be a Request" in str(e.value)

    def test_if_returns_test_when_input_is_a_get_input(self, request_port: RequestPort):
        input = Request(
            request_line=RequestLine(
                method=MethodEnum.GET,
                path="/",
                http_version="HTTP/1.0"
            ),
            headers=[
                BaseHeader(name="Host", value="localhost")
            ]
        )
        assert request_port.get(input) == "test"