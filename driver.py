import requests

token = ''

parameters = {'access_token': token}

resp = requests.get('https://graph.facebook.com/v2.3/me/friends?limit=100&fields=name,location', params = parameters)
jsonData = resp.json()

noLocation = []

for elem in jsonData["data"]:
	if "location" in elem:
		print elem["name"]
		print elem["location"]
	else:
		noLocation.append(elem["name"])

print "Those without any location\n\n"

for elem in noLocation:
	print elem
