from building_web_browser_from_scratch.core.models import *
from building_web_browser_from_scratch.adapters.requests import SocketHTTPSRequest

hostname = "browser.engineering"
request = Request(
    request_line=RequestLine(
        method=MethodEnum.GET,
        http_version="HTTP/1.0",
        path="/examples/xiyouji.html"
    ),
    headers=[
        BaseHeader(name="Host", value=hostname)
    ]
)

if __name__ == "__main__":
    response = SocketHTTPSRequest().send_request(input=request, to=Destiny(port=443, hostname=hostname))
    print(response)

# import tkinter 

# WIDTH = 800
# HEIGHT = 600

# class Browser:
#     def __init__(self):
#         self.window = tkinter.Tk()
#         self.canvas = tkinter.Canvas(
#             self.window,
#             width=WIDTH,
#             height=HEIGHT
#         )
#         self.canvas.pack()

#     def load(self, url):
#         self.canvas.create_rectangle(10, 20, 400, 300)
#         self.canvas.create_oval(100, 100, 150, 150)
#         self.canvas.create_text(200, 150, text="Hi!")

# if __name__ == "__main__":
#     import sys
#     Browser().load('hello world!')
#     tkinter.mainloop()
