import gis_token_generator
import datetime
import requests


class GetContacts:

	def __init__(self, email, password,date):
		token_generation = gis_token_generator.GISTokenGenerator(email, password)
		self.token = token_generation.generate_token()
		self.now = date
	#

	def getApps(self):
		url = "https://gis-api.aiesec.org/v2/applications.json"

		end_date = self.now.strftime('%y-%m-%d')
		params = {
		"access_token" : self.token,
		"filters[opportunity_committee]" : 1589,
		"filters[last_interaction][from]" : self.now.strftime('%y-%m-%d'),
		"filters[last_interaction][to]" : self.now.strftime('%y-%m-%d')
		}

		#	url_op = 'https://gis-api.aiesec.org/v2/people.json?access_token='+ access_token+ '&filters%5Bregistered%5Bfrom%5D%5D=' + start_date + '&filters%5Bregistered%5Bto%5D%5D=' + end_date+'&filters%5Bcommittee_scope%5D='
		q = requests.get(url, data=params)
		print q.text




cont = GetContacts("enrique.suarez@aiesec.net","si no leo me aburro",datetime.datetime.now())
cont.getApps()
