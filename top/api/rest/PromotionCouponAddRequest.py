'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class PromotionCouponAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.condition = None
		self.denominations = None
		self.end_time = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.promotion.coupon.add'
