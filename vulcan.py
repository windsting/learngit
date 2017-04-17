#!/usr/bin/env python

# a HTTP server

import sys
import SimpleHTTPServer
import SocketServer

# print sys.argv

PORT = 8000
if len(sys.argv) > 1 :
	PORT = int(sys.argv[1])

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

