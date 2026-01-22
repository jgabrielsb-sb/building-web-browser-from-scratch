from pydantic import BaseModel
from .enum import SchemesEnum

class URL(BaseModel):
    scheme: SchemesEnum
    hostname: str
    path: str

    