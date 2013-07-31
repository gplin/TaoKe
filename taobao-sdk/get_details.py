# -*- coding: utf-8 -*-
"""
Created: 2013-02-16
Author: gplin
"""
import top.api

req = top.api.TaobaokeItemsDetailGetRequest("gw.api.tbsandbox.com")
req.set_app_info(top.appinfo("1021039194","sandboxa7f002adf21ae4ec28f4fdb65"))
req.pid = 30462502
req.outer_code = "gplin"
req.num_iids = "1500006950787"
req.fields = "click_url,shop_click_url,detail_url,type,seller_credit_score,num_iid,title,nick"

try:
    f = req.getResponse()
    #print f
except Exception,e:
    print e
