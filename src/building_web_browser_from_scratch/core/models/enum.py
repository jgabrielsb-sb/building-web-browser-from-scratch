from enum import Enum

class SchemesEnum(Enum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"

class MethodEnum(Enum):
    GET = "GET"
    POST = "POST"
    UPDATE = "UPDATE"
    PATCH = "PATCH"
    DELETE = "DELETE"