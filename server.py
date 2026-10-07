#!/usr/bin/env python3
import http.server
import ssl
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

httpd = http.server.HTTPServer(('localhost', 8000), MyHTTPRequestHandler)
print("서버 시작: http://localhost:8000")
print("Ctrl+C로 중지")

httpd.serve_forever()
