'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class SubuserDutyUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.duty_id = None
		self.duty_level = None
		self.duty_name = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.subuser.duty.update'
