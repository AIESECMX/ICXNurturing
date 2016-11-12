import gis_token_generator
import datetime
import requests


def getToken (user, passw):
	url = "https://aiesec.org.mx/gis_session.php"
	params = {
	"user" : user,
	"pass" : passw
	}
	q = requests.post(url, data=params)
	return q.text


print getToken("enrique.suarez@aiesec.net","si no leo me aburro")
