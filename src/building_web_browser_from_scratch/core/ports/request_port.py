from abc import abstractmethod, ABC
from building_web_browser_from_scratch.core.models import Request
from building_web_browser_from_scratch.core.exceptions import RequestPortException

class RequestPort(ABC):
    @abstractmethod
    def _get(self, input: Request):
        pass

    def get(self, input: Request):
        if not isinstance(input, Request):
            raise TypeError('input must be a Request')

        try:    
            return self._get(input)
        except Exception as e:
            raise RequestPortException(f"Error on get request: {e}")

    