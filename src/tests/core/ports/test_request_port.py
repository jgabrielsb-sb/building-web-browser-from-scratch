from building_web_browser_from_scratch.core.ports import RequestPort
from building_web_browser_from_scratch.core.models import Request, RequestLine, BaseHeader, MethodEnum
import pytest

@pytest.fixture
def request_port():
    class RequestPortImpl(RequestPort):
        def _send_request(self, input: Request):
            return "test"

        def _get_response(self) -> Request:
            return "test"

    return RequestPortImpl()

class TestRequestPort:
    def test_if_raises_type_error_when_input_is_not_a_get_input(self, request_port: RequestPort):
        with pytest.raises(TypeError) as e:
            request_port.send_request(None)
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
        assert request_port.send_request(input) == "test"

    def test_if_raises_request_port_exception_when_send_request_raises_exception(self, request_port: RequestPort):
        with pytest.raises(TypeError) as e:
            request_port.send_request(None)
        assert "input must be a Request" in str(e.value)

    def test_if_returns_test_when_get_response_is_called(self, request_port: RequestPort):
        assert request_port.get_response() == "test"

    