# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import csv

from settings import *


def load_data():
    result = {}
    # Load data from csv file
    with open(data_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Each record has three columns: word, part of speech, definition
        # Create a dictionary key as needed, and the value is a list of definitions such as [["definition", "part of speech"],...]
        for row in reader:
            lower_row = row[0].lower()
            if lower_row not in result:
                result[lower_row] = []
            result[lower_row].append([row[1], row[2]])
    return result


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        if data.get(self.path[1:].lower()) is not None:
            self.wfile.write(bytes("<p>%s</p>" % self.path[1:], "utf-8"))
            for i in data[self.path[1:].lower()]:
                self.wfile.write(bytes("<p>%s - %s</p>" % (i[0], i[1]), "utf-8"))
        else:
            self.wfile.write(bytes("<p>%s is undefined</p>" % self.path[1:], "utf-8"))
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
