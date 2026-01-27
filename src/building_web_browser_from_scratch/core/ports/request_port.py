from abc import abstractmethod, ABC
from building_web_browser_from_scratch.core.models import Request, Response
from building_web_browser_from_scratch.core.exceptions import RequestPortException
from building_web_browser_from_scratch.core.models.ports.dto_request import Destiny

class RequestPort(ABC):
    @abstractmethod
    def _send_request(self, input: Request, to: Destiny):
        pass

    def send_request(self, input: Request, to: Destiny) -> Response:
        if not isinstance(input, Request):
            raise TypeError('input must be a Request')

        try:    
            return self._send_request(input, to)
        except Exception as e:
            raise RequestPortException(f"Error on send request: {e}")

    @abstractmethod
    def _get_response(self) -> Request:
        pass

    def get_response(self) -> Request:
        try:
            return self._get_response()
        except Exception as e:
            raise RequestPortException(f"Error on get response: {e}")
    


    