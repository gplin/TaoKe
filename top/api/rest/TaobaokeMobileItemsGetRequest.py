'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class TaobaokeMobileItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.area = None
		self.auto_send = None
		self.cash_coupon = None
		self.cash_ondelivery = None
		self.cid = None
		self.end_commissionNum = None
		self.end_commissionRate = None
		self.end_credit = None
		self.end_price = None
		self.end_totalnum = None
		self.fields = None
		self.guarantee = None
		self.keyword = None
		self.mall_item = None
		self.onemonth_repair = None
		self.outer_code = None
		self.overseas_item = None
		self.page_no = None
		self.page_size = None
		self.real_describe = None
		self.refer_type = None
		self.sevendays_return = None
		self.sort = None
		self.start_commissionNum = None
		self.start_commissionRate = None
		self.start_credit = None
		self.start_price = None
		self.start_totalnum = None
		self.vip_card = None

	def getapiname(self):
		return 'taobao.taobaoke.mobile.items.get'
