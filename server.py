#!/usr/bin/env python
import os
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

light = True

class MyHandler(SimpleHTTPRequestHandler):

  def do_POST(self):
    global light
    self.send_response(200)
    self.send_header('Content-type','application/json')
    self.end_headers()

    if light:
      light = False
      self.wfile.write("{\"status\": true }")
    else:
      light = True
      self.wfile.write("{\"status\": false}")

if __name__ == '__main__':
    HTTPServer(('0.0.0.0', 8080), MyHandler).serve_forever()
