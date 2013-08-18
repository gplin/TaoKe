# -*- coding: utf-8 -*-
"""
Created: 2013-02-16
Author: gplin
Desc: 分享宝贝
"""
import re
##import topsettings
import top.api

def extract_num_iid(url):
	"""
	parameter: str: url字符串 or list 类型,从传入的参数(url)中提取宝贝的ID:num
	return   : list
	"""
	result = []
	urllist = url if isinstance(url,list) else list(url)
	pattern_id = re.compile(r'id=\d{1,}(\s|\S)?',re.I)
	pattern_num = re.compile(r'\d{1,}',re.I)

	for current_url in urllist:
		match = pattern_id.search(current_url)
		if match:
			iid = match.group()
			num = pattern_num.search(iid).group()
			result.append(num)
	return result


##def GetDetail(num_iids):
##	req = top.api.TaobaokeItemsDetailGetRequest(topsettings.domain(1))
##	req.set_app_info(top.appinfo(topsettings.appkey(),topsettings.secret(1) ))
##	req.pid = topsettings.PID()
##	req.outer_code = "gplin"
##	req.num_iids = num_iids
##	req.fields = "click_url,shop_click_url,detail_url,type,seller_credit_score,num_iid,title,nick"
##
##	try:
##	    f = req.getResponse()
##	except Exception,e:
##	    print e
