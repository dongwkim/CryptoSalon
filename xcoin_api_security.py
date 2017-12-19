import csv 

## Get API key and secret from local file
def getKey(key_path):
	with open(key_path) as key:
		keys = csv.DictReader(key, delimiter=',')
		for c in keys:
			api_key = c['key']
			api_secret = c['secret']
	key.close()
	return api_key,api_secret
