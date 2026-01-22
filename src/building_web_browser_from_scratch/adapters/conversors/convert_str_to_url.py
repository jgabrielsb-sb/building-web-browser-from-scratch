
from building_web_browser_from_scratch.core.ports import ConversorPort
from building_web_browser_from_scratch.core.models import URL

class ConvertStrToUrl(ConversorPort):
    def _run(self, input: str) -> URL:
        if not isinstance(input, str):
            raise TypeError('input must be a str')

        return None

    

        

