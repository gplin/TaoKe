'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class HotelOrderBookingFeedbackRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.failed_reason = None
		self.message_id = None
		self.oid = None
		self.out_oid = None
		self.refund_code = None
		self.result = None
		self.session_id = None

	def getapiname(self):
		return 'taobao.hotel.order.booking.feedback'
