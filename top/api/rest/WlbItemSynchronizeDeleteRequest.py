'''
Created by auto_sdk on 2013-09-15 12:51:27
'''
from top.api.base import RestApi
class WlbItemSynchronizeDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ext_entity_id = None
		self.ext_entity_type = None
		self.item_id = None

	def getapiname(self):
		return 'taobao.wlb.item.synchronize.delete'
