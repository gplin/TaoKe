'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class UdpJuhuasuanGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.begin_time = None
		self.catid = None
		self.end_time = None
		self.fields = None
		self.itemid = None
		self.parameters = None

	def getapiname(self):
		return 'taobao.udp.juhuasuan.get'
