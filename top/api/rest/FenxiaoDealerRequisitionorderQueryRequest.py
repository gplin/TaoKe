'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class FenxiaoDealerRequisitionorderQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.dealer_order_ids = None
		self.fields = None

	def getapiname(self):
		return 'taobao.fenxiao.dealer.requisitionorder.query'
