import requests

class Client:

	def __init__(self, hostname):
		self.hostname = hostname
		self.headers = {
  		'Content-Type': 'application/vnd.api+json',
  		'Accept': 'application/vnd.api+json'
		}

	def search(self, format = None, tags = None):
		criteria = {}
		if format is not None:
			criteria['format'] = format
		if tags is not None:
			criteria['tags'] = tags
		response = requests.get(self.hostname + '/data', params=criteria, headers=self.headers)
		return response.json()
