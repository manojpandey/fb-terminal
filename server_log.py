import SimpleHTTPServer
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler as BaseHTTPRequestHandler
import sys
import os
import requests
import webbrowser
import time
import subprocess
import threading
PORT = 7777 # Make sure the port is noot in use with some other app

def start_server():
	'''class MyHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	    log_file = open('logfile.txt', 'w')
	    def log_message(self, format, *args):
	        self.log_file.write("%s\n" % (format%args))

	Handler = MyHTTPHandler

	httpd = SocketServer.TCPServer(("", PORT), Handler)

	print "serving at port", PORT

	httpd.serve_forever()'''

	server = HTTPServer(('localhost', PORT), BaseHTTPRequestHandler)
	thread = threading.Thread(target = server.serve_forever)
	thread.deamon = True

def up():
	start_server()
	thread.start()
	print "Starting"

def down():
	server.shutdown()
	print "Closing"


""" Get access token parsed from the server log response """
def getAccessTokenParsed():
	myfile = open('/Users/ankitsultana/GitHub/fb-terminal/logfile.txt')
	return list(myfile)[0][12:-16]


""" Getting the Oauth token by authorizing the app """
def getOAuthToken():
	url = "https://www.facebook.com/v2.2/dialog/oauth?client_id=1176148169078022&scope=public_profile&response_type=code&redirect_uri=http://localhost:7777"
	webbrowser.open(url, new=1, autoraise=True)
	#webbrowser.open(url)

	# Improve this part
	up()
	time.sleep(2)
	down()

	# get the access token from the redirected url received on server
	a_token = getAccessTokenParsed()

	print a_token

	# returning oauth token
	return str(a_token) 


""" Getting the access_token using the OAuth token """
def getAccessToken(oauth_token):
	new_url = "https://graph.facebook.com/oauth/access_token?client_id=1176148169078022&client_secret=a623b10331c1246be41c7eaa9f78c481&code="+oauth_token+"&redirect_uri=http://localhost:7777/"
	print new_url
	resp = requests.get(new_url)
	a = resp.content # all text content
	print a[13:-16]
	acc_token = a[13:-16]
	return acc_token

def getUserDetails(access_token):

    url = "https://graph.facebook.com/me?access_token="+access_token;
    resp = requests.get(url)
    jsonData = resp.json()
    print "\n\n"
    print "Welcome " + jsonData["name"]
    print "Your User ID: " + jsonData["id"]
    print "Your access token (keep it safe): " + str(access_token)

""" Main Function"""
def main():
	a_token = getOAuthToken()
	access_token = getAccessToken(a_token)

	getUserDetails(access_token)

if __name__ == "__main__":
	main()
