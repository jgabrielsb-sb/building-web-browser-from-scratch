import socket
from building_web_browser_from_scratch.adapters.requests import SocketHTTPSRequest
from building_web_browser_from_scratch.core.models import *

s = SocketHTTPSRequest()

request = Request(
    request_line=RequestLine(
        method=MethodEnum.GET,
        path="/",
        http_version="HTTP/1.1"
    ),
    headers=[
        BaseHeader(
            name="Host", value="example.com"
        )
    ]
)

response = s.send_request(request, Destiny(url="example.com", port=443))

print(response)
