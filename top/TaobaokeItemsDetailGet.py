# -*- coding: utf-8 -*-
"""
Created: 2013-02-16
Author: gplin
Desc: 调用API(taobao.taobaoke.items.detail.get)查询淘宝客推广商品详细信息
"""
import re
import top.settings as settings
# import top.api
from top.api import	TaobaokeItemsDetailGetRequest

def extract_num_iid(url):
	"""
	desc: 从传入的参数(url)中提取商品的ID:num
	parameter: url字符串 or url 列表(list类型)
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


def GetDetail(num_iids):
	req = TaobaokeItemsDetailGetRequest(settings.domain(1))
	req.set_app_info(top.appinfo(settings.appkey(),settings.secret(1) ))
	req.pid = settings.PID()
	req.outer_code = "gplin"
	req.num_iids = num_iids
	req.fields = "click_url,shop_click_url,detail_url,type,seller_credit_score,num_iid,title,nick"

	try:
	    f = req.getResponse()
	except Exception,e:
	    print e
	return f