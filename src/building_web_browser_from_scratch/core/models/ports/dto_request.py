from pydantic import BaseModel
from building_web_browser_from_scratch.core.models import MethodEnum

class RequestLine(BaseModel):
    method: MethodEnum
    http_version: str = "HTTP/1.0"
    path: str

class BaseHeader(BaseModel):
    name: str
    value: str

class Request(BaseModel):
    request_line: RequestLine
    headers: list[BaseHeader]
    





