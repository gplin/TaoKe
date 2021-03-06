'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class TaobaokeMobileItemsCouponGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.area = None
		self.cid = None
		self.coupon_type = None
		self.end_commission_num = None
		self.end_commission_rate = None
		self.end_commission_volume = None
		self.end_coupon_rate = None
		self.end_credit = None
		self.end_volume = None
		self.fields = None
		self.keyword = None
		self.outer_code = None
		self.page_no = None
		self.page_size = None
		self.refer_type = None
		self.shop_type = None
		self.sort = None
		self.start_commission_num = None
		self.start_commission_rate = None
		self.start_commission_volume = None
		self.start_coupon_rate = None
		self.start_credit = None
		self.start_volume = None

	def getapiname(self):
		return 'taobao.taobaoke.mobile.items.coupon.get'
