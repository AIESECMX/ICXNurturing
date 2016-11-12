import datetime
import requests





	#

	def getApps():
		url = "https://gis-api.aiesec.org/v2/applications.json"
		now = datetime.datetime.now()
		end_date = now.strftime('%y-%m-%d')
		params = {
		"access_token" : getToken(,) ,
		"filters[opportunity_committee]" : 1589,
		"filters[status]": "rejected"
		"filters[last_interaction][from]" : self.now.strftime('%y-%m-%d'),
		"filters[last_interaction][to]" : self.now.strftime('%y-%m-%d')
		}

		#	url_op = 'https://gis-api.aiesec.org/v2/people.json?access_token='+ access_token+ '&filters%5Bregistered%5Bfrom%5D%5D=' + start_date + '&filters%5Bregistered%5Bto%5D%5D=' + end_date+'&filters%5Bcommittee_scope%5D='
		q = requests.get(url, data=params)
		print q.text







		def getToken (user, passw):
			url = "https://aiesec.org.mx/gis_session.php"
			params = {
			"user" : user,
			"pass" : passw
			}
			q = requests.post(url, data=params)
			return q.text


#
print getApps();



