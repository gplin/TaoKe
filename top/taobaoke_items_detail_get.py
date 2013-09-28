# -*- coding: utf-8 -*-
"""
Created: 2013-02-16
Author: gplin
Desc: 调用API(taobao.taobaoke.items.detail.get)查询淘宝客推广商品详细信息
"""
import re
from share.models import Item
import top
from top.base import downLoad_item_pic
from top.api import TaobaokeItemsDetailGetRequest

API_RESPONSE_KEY = ['taobaoke_items_detail_get_response','taobaoke_item_details','taobaoke_item_detail']

def extract_num_iid(url):
    """
    desc: 从传入的参数(url)中提取商品的ID:num
    parameter: url字符串 or url 列表(list类型)
    return   : list
    """
    result = []
    urllist = url if isinstance(url,list) else [url]
    pattern_id = re.compile(r'id=\d{1,}(\s|\S)?',re.I)
    pattern_num = re.compile(r'\d{1,}',re.I)

    for current_url in urllist:
        match = pattern_id.search(current_url)
        if match:
            iid = match.group()
            num = pattern_num.search(iid).group()
            result.append(num)
    return result


def get_detail(num_iids):
    req = TaobaokeItemsDetailGetRequest(top.domain(1))
    req.set_app_info(top.appinfo(top.appkey(),top.secret(1) ))
    req.pid = top.PID()
    req.outer_code = "gplin"
    req.num_iids = num_iids
    req.fields = "click_url,shop_click_url,detail_url,type,seller_credit_score,num_iid,title,nick,desc"

    # get the data
    response = req.getResponse()
    if response.has_key(API_RESPONSE_KEY[0]):
        if response[API_RESPONSE_KEY[0]].has_key(API_RESPONSE_KEY[1]):
            data=response[API_RESPONSE_KEY[0]][API_RESPONSE_KEY[1]]
            # total_results = data["total_results"]
            item_detail = data[API_RESPONSE_KEY[2]]
            return item_detail
            # return data
    return None

def test_share_item(url):
    ""
    print "begin get %s" % url
    num_iids = extract_num_iid(url)
    for id in num_iids:
        print "----------"
        data=get_detail(id)
        # print data
        for item in data:
            # download pic
            print item["item"]["pic_url"]
            pic=downLoad_item_pic(item["item"]["pic_url"])
            temp=Item.objects.save_item_from_detail_get(account_id=1,data=item,pic=pic)
            print "done %s" % temp.num_iid
            return temp
    print "done test share"
