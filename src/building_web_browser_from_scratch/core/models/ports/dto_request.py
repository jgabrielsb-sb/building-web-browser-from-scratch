from pydantic import BaseModel
from building_web_browser_from_scratch.core.models import MethodEnum

class Request(BaseModel):
    method: MethodEnum 
    hostname: str
    path: str
    content: str | None

class GetInput(Request):
    method: MethodEnum = MethodEnum.GET

    @property
    def get_method(self) -> MethodEnum:
        return MethodEnum.GET



