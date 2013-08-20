# -*- coding:utf-8 -*-
from top import TaobaokeItemsDetailGet


# =============top api global settings================
# class settings(object):
# 	"""
# 	top api global settings
# 	"""
# 	domain = "gw.api.taobao.com"

# 调用入口
# 正式环境: http://gw.api.taobao.com/router/rest
# 沙箱环境: http://gw.api.tbsandbox.com/router/rest
def domain(issandbox=None):
	"""
	"""
	return 'gw.api.taobao.com' if not issandbox else 'gw.api.tbsandbox.com'

# default appkey and secret
def appkey():
	"""
	return default appkey
	"""
	return unicode('1021039194')

def secret(issandbox=None):
	"""
	issandbox: boolean
	return secret if not issandbox else sandboxSecret
	"""
	return '' if not issandbox else 'sandboxa7f002adf21ae4ec28f4fdb65'

# 淘宝客PID: mm_30462502_0_0
def PID():
	"""
	return taobaoke PID num
	"""
	return 30462502 
# ====================================================

class appinfo(object):
   def __init__(self,appkey,secret):
       self.appkey = appkey
       self.secret = secret
       
def getDefaultAppInfo():
   pass

    
def setDefaultAppInfo(appkey,secret):
   default = appinfo(appkey,secret)
   global getDefaultAppInfo 
   getDefaultAppInfo = lambda: default
    




    

