'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class AlipayTopatsUserAccountreportGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.charset = None
		self.end_time = None
		self.fields = None
		self.start_time = None
		self.type = None

	def getapiname(self):
		return 'alipay.topats.user.accountreport.get'
