"""
Generic class that provides an interface for
converting a certain object to another
"""
from abc import abstractmethod, ABC
from building_web_browser_from_scratch.core.exceptions import ConversorPortException

class ConversorPort(ABC):

    @abstractmethod
    def _run(self, input: any) -> any:
        pass

    def run(self, input: any) -> any:

        try:
            return self._run(input)
        except Exception as e:
            raise ConversorPortException(f"Error on conversor: {e}")
