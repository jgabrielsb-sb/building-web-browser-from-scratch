from abc import abstractmethod, ABC
from building_web_browser_from_scratch.core.models import GetInput
from building_web_browser_from_scratch.core.exceptions import RequestPortException

class RequestPort(ABC):
    @abstractmethod
    def _get(self, input: GetInput):
        pass

    def get(self, input: GetInput):
        if not isinstance(input, GetInput):
            raise TypeError('input must be a GetInput')

        try:    
            return self._get(input)
        except Exception as e:
            raise RequestPortException(f"Error on get request: {e}")

    