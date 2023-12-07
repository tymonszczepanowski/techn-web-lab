#!/bin/env python3
import http.server
import json

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(open("index.html", "rb").read())
        elif self.path == "/api/author":
            data = {"name": "Tymon Szczepanowski", "indeks": "180511"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_error(404)

if __name__ == "__main__":
    server = http.server.HTTPServer(("", 8080), MyHandler)
    server.serve_forever()

