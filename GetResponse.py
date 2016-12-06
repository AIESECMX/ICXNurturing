import requests
import socket
import json

#
class GetResponse(object):

	def __init__(self):
		super(GetResponse, self).__init__()
		self.url ='https://api3.getresponse360.com/v3'
		self.gr_id='api-key edd91283845856ad6863a3ee76a421c9'
		self.gr_api_domain = 'aiesec.getresponse360.com'
		




	#
	def custom_fields(self):
		headers = {'X-Auth-Token':self.gr_id,'X-Domain':self.gr_api_domain}
		q = requests.get(self.url+'/custom-fields', headers=headers)
		print q.content
		pass

	#
	#Get Response
	#Get Response
	#Get Response

	#Status - Open - iGV
	def sendOpenIGV(self):
		data = {'name':'ep.name',
		'email':'vampa@ciencias.unam.mx',
		'campaign':{
		'campaignId': 'SbOFA'
		},
		'dayOfCycle':'0',
		'customFieldValues':[
				{'customFieldId':'zDYKh','value':['http://image.shutterstock.com/z/stock-vector-lol-87079871.jpg']},# ep foto
				{'customFieldId':'zDYKE','value':['opp.name']},#opp name
				{'customFieldId':'zDYK1','value':['opp.city']},#op city
				{'customFieldId':'zDYKT','value':['opp.sdg']}#op sdg
				]

				}
		#
		#
		headers = {'X-Auth-Token':self.gr_id,'X-Domain':self.gr_api_domain,'Content-Type':'application/json'}
		q = requests.post(self.url+'/contacts', headers=headers,data=json.dumps(data))
		print q.content

		return None

	#Status - Open - iGT
	def endopenIGT(self,ep, opp,opp1,opp2,opp3):
		return None

	# Status - Open - iGE
	def sendOpenIGE(self,ep, opp,opp1,opp2,opp3):
		return None
	# Status - Open - All programs (for EP manager)
	def sendToManager(self,ep, manager, opp):
		return None
	#Status - Rejected - iGV
	def sendRejectediGV(self,ep, opp,opp1,opp2,opp3):
		return None

	#Status - Rejected - iGT
	def sendRejectediGT(self,ep, opp,opp1,opp2,opp3):
		return None
	#Status - Rejected - iGE
	def sendRejectediGE(self,ep, opp,opp1,opp2,opp3):
		return None



#
print 'antes'
gr = GetResponse()

gr.custom_fields()
gr.sendOpenIGV()
print 'despues'