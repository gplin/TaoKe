'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class CrmGroupAppendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.from_group_id = None
		self.to_group_id = None

	def getapiname(self):
		return 'taobao.crm.group.append'
