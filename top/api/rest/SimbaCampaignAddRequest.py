'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class SimbaCampaignAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.nick = None
		self.title = None

	def getapiname(self):
		return 'taobao.simba.campaign.add'
