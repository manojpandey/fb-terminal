import SimpleHTTPServer
import SocketServer
import sys

PORT = 7777

class MyHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    log_file = open('logfile.txt', 'w')
    def log_message(self, format, *args):
        self.log_file.write("%s\n" %
                            (format%args))

Handler = MyHTTPHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT

httpd.serve_forever()