import socket

from building_web_browser_from_scratch.core.models import *
from building_web_browser_from_scratch.adapters.conversors import ConvertRequestToStr
from building_web_browser_from_scratch.adapters.requests import SocketHTTPRequest
HOST = "example.com"
PORT = 80

request = (
    "GET / HTTP/1.1\r\n"
    "Host: example.com\r\n"
    "User-Agent: socket-learning-client/1.0\r\n"
    "Accept: */*\r\n"
    "Connection: close\r\n"
    "\r\n"
)
request = Request(
    request_line=RequestLine(
        method=MethodEnum.GET,
        path="/",
        http_version="HTTP/1.0"
    ),
    headers=[
        BaseHeader(name="Host", value="example.com"),
        #BaseHeader(name="User-Agent", value="socket-learning-client/1.0"),
        #BaseHeader(name="Accept", value="*/*"),
        #BaseHeader(name="Connection", value="close"),
    ]
)

socket_http_request = SocketHTTPRequest()
response = socket_http_request.send_request(request, Destiny(url="example.com", port=80))
print(response.content)

# convert_request_to_str = ConvertRequestToStr().run(request)

# print("=== REQUEST ===")
# #print(request.replace("\r", "\\r").replace("\n", "\\n\n"))

# with socket.create_connection((HOST, PORT), timeout=10) as s:
#     s.sendall(convert_request_to_str.encode("utf-8"))

#     response = b""
#     while True:
#         data = s.recv(4096)
#         if not data:
#             break
#         response += data

# print("\n=== RAW RESPONSE ===")
# print(response.decode("iso-8859-1"))
