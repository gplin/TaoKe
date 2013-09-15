'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class AlipayMicropayOrderGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.alipay_order_no = None
		self.auth_token = None

	def getapiname(self):
		return 'alipay.micropay.order.get'
