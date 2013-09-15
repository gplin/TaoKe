'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class CrmMembersIncrementGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.current_page = None
		self.end_modify = None
		self.grade = None
		self.page_size = None
		self.start_modify = None

	def getapiname(self):
		return 'taobao.crm.members.increment.get'
