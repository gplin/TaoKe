'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class HanoiGroupFilterRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.buyer_nick = None
		self.group_id = None
		self.seller_nick = None

	def getapiname(self):
		return 'taobao.hanoi.group.filter'
