'''
Created by auto_sdk on 2013-02-15 16:36:21
'''
from top.api.base import RestApi
class UserBuyerGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None

	def getapiname(self):
		return 'taobao.user.buyer.get'