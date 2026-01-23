from building_web_browser_from_scratch.core.ports import RequestPort
from building_web_browser_from_scratch.core.models import GetInput
import pytest

@pytest.fixture
def request_port():
    class RequestPortImpl(RequestPort):
        def _get(self, input: GetInput):
            return "test"
    return RequestPortImpl()

class TestRequestPort:
    def test_if_raises_type_error_when_input_is_not_a_get_input(self, request_port: RequestPort):
        with pytest.raises(TypeError) as e:
            request_port.get(None)
        assert "input must be a GetInput" in str(e.value)

    def test_if_returns_test_when_input_is_a_get_input(self, request_port: RequestPort):
        input = GetInput(
            hostname="www.example.com",
            path="/",
            content=None
        )
        assert request_port.get(input) == "test"