#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, requests, webbrowser, time, subprocess, threading

# Server imports
import SimpleHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler 
from BaseHTTPServer import HTTPServer

# PORT to be used
PORT = 7777

class CustomHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	logFile = open('logfile.txt', 'w')
	def log_message(self, format, *args):
		self.logFile.write("%s\n" % (format%args))
		self.logFile.close()

server = HTTPServer(('localhost', PORT), CustomHTTPHandler)
class Fbcli:


	def startServer(self):	
		thread = threading.Thread(target = server.serve_forever)
		thread.deamon = True
		thread.start()

	def getOAuthCode(self):
		url = 'https://www.facebook.com/v2.2/dialog/oauth?client_id=1176148169078022&scope=public_profile&response_type=code&redirect_uri=http://localhost:7777'
		print url+'\n'
		webbrowser.open(url, new=1, autoraise=True)
		self.startServer()
		
		print "Login in 10 seconds: "+"\n"
		time.sleep(10)
		self.stopServer()
		x = self.getCodeParsed()	
		print "Shit under"
		print x 
		print "\n\nDonw\n\n"
		return x

	def getCodeParsed(self):
		myFile = open('logfile.txt', 'r')
		#print list(myFile)
		content = str(myFile.read())
		x = content[12:-16].rstrip()
		return x

	def getAccessTokenFromCode(self, OAuthCode):
		codeurl = 'https://graph.facebook.com/oauth/access_token?client_id=1176148169078022&client_secret=a623b10331c1246be41c7eaa9f78c481&code='+OAuthCode+'&redirect_uri=http://localhost:7777/'
		print codeurl + '\n'
		resp = requests.get(codeurl)
		respContent = resp.content
		print "Access_token donw: "
		print respContent[13:-16]
		return respContent[13:-16]

	def getUserDetails(self, accessToken):
		url = 'https://graph.facebook.com/v2.3/me?access_token='+accessToken
		resp = requests.get(url)
		jsonData = resp.json()
		print "Welcome " + jsonData["name"]
		print "Your User ID: " + jsonData["id"]
		print "Your access token (keep it safe): " + str(accessToken)
		print "Thanks dumbass i have your password"
	
	def storeCredential(self):
		pass

	def stopServer(self):
		server.shutdown()
	
def main():
	test = Fbcli()
	code = test.getOAuthCode()
	accessToken = test.getAccessTokenFromCode(code)
	test.getUserDetails(accessToken)

if __name__ == "__main__":
	main()
