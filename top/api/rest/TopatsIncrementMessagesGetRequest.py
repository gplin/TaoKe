'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class TopatsIncrementMessagesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end = None
		self.start = None
		self.topics = None

	def getapiname(self):
		return 'taobao.topats.increment.messages.get'
