# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from server.settings import host_name, server_port
from server.core import load_data


class MyServer(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        if data.get(self.path[1:].lower()) is not None:
            print("Here we are")
            self.wfile.write(bytes("<p>%s</p>" % self.path[1:], "utf-8"))
            for i in data[self.path[1:].lower()]:
                self.wfile.write(bytes("<p>%s - %s</p>" % (i[0], i[1]), "utf-8"))
        else:
            self.wfile.write(bytes("<p>%s</p>" % self.path[1:], "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    data = load_data()
    webServer = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("\nServer stopped.")
