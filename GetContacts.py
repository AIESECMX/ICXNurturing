import datetime
import requests






def getApps():
	url = "https://gis-api.aiesec.org/v2/applications.json"
	now = datetime.datetime.now()
	end_date = now.strftime('%y-%m-%d')
	params = {
	"access_token" : getToken("enrique.suarez@aiesec.net","si no leo me aburro") ,
	"filters[opportunity_committee]" : 1589,
	"filters[status]": "rejected",
	"filters[last_interaction][from]" :now.strftime('%y-%m-%d'),
	"filters[last_interaction][to]" : now.strftime('%y-%m-%d')
	}


	q = requests.get(url, data=params)
	print q.text






#
def getToken (user, passw):
	url = "https://aiesec.org.mx/gis_session.php"
	params = {
	"user" : user,
	"pass" : passw
	}
	q = requests.post(url, data=params)
	return q.text


#Get Response
#Get Response
#Get Response

#Status - Open - iGV
def sendOpenIGV(ep, opp,opp1,opp2,opp3):
	return None

#Status - Open - iGT
def endopenIGT(ep, opp,opp1,opp2,opp3):
	return None

# Status - Open - iGE
def sendOpenIGE(ep, opp,opp1,opp2,opp3):
	return None
# Status - Open - All programs (for EP manager)
def sendToManager(ep, manager, opp):
	return None
#Status - Rejected - iGV
def sendRejectediGV(ep, opp,opp1,opp2,opp3):
	return None

#Status - Rejected - iGT
def sendRejectediGT(ep, opp,opp1,opp2,opp3):
	return None
#Status - Rejected - iGE
def sendRejectediGE(ep, opp,opp1,opp2,opp3):
	return None

sendRejectediGE(ep= ugdugfs, opp2 = usydgfugys)

#Get Response
#Get Response
#Get Response

#
getApps();



