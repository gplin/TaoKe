'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class RdsDbGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.db_status = None
		self.instance_name = None

	def getapiname(self):
		return 'taobao.rds.db.get'
