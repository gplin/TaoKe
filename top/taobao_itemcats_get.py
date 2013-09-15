# -*- coding: utf-8 -*-
"""
Created: 2013-02-16
Author: gplin
Desc: 类目API, 提供了标准类目,类目属性和类目属性值的查询功能
      taobao.itemcats.authorize.get     查询商家被授权品牌列表和类目列表
      taobao.itemcats.get               获取后台供卖家发布商品的标准商品类目
      taobao.itemcats.increment.get     增量获取后台类目数据
      taobao.itemprops.get              获取标准商品类目属性
      taobao.itempropvalues.get         获取标准类目属性值
      taobao.topats.itemcats.get        全量获取后台类目数据
"""
import os
import re
import sqlite3
from django.conf import settings

import utils
import top
from top.api import ItemcatsGetRequest,TopatsItemcatsGetRequest,TopatsResultGetRequest

API_RESPONSE_KEY = "itemcats_get_response"

error =[]

def item_cats_get(parent_cid,cids=None):
    """
    应用级输入参数:
    fields:
    parent_cid:
    cids:
    """ 
    try:
        req = ItemcatsGetRequest(top.domain(1))
        req.set_app_info(top.appinfo(top.appkey(),top.secret(1) )) 

        req.fields = "cid,parent_cid,name,is_parent,status,sort_order"
        req.parent_cid = parent_cid
        req.cids = cids

        # get the data
        response = req.getResponse()
        if response.has_key(API_RESPONSE_KEY):
            data = response[API_RESPONSE_KEY]
            if data["item_cats"].has_key("item_cat"):
                result = data["item_cats"]["item_cat"]
                return result
        return None
    except Exception,e:
        print e,
        error.append(parent_cid)
        return None

def add_item_cats(data):
    u"""保存类目数据"""
    if data is None:
        raise ValueError(u'data must be set')
    is_list = isinstance(data,list)
    if not is_list and not isinstance(data,dict):
        raise ValueError(u'data must be list or dict ')
    data = data if is_list else [data]
    conn = sqlite3.connect(os.path.join(settings.PROJECT_DIR,"db\TaoKe.db"))
    cur= conn.cursor()

    for item in data:
        cur.execute("""
              Insert Into share_item_cats(
               cid,
               is_parent,
               name,
               parent_cid,
               status,
               sort_order,
               enable
              ) values(
                ?,?,?,?,?,?,?
              )
              """,(item["cid"],item["is_parent"],item["name"],
                   item["parent_cid"],item["status"],item["sort_order"],0))
        conn.commit()
        # print "commit %s" % item["cid"]
    cur.close()

def get_subitemcats():
    conn = sqlite3.connect(os.path.join(settings.PROJECT_DIR,"db\Taoke.db"))
    cursor = conn.cursor()
    parent_cid_list = cursor.execute("select cid from share_item_cats where is_parent=1 order  by cid")
    cid=[]
    for row in parent_cid_list:
        cid.append(row[0])
    cursor.close()


    i=1
    for id in cid:
        data=item_cats_get(id)
        print "begin sql %s, cid : %s" % (i,id)
        if data:
            add_item_cats(data)
            
            print "%s done %s" % (id,i)
        i=i+1

def main():
    print "begin"
    data = item_cats_get(0)
    add_item_cats(data)
    print "done parent =0"
    # temp(data)
    # print "done all"


def temp(data):
    cid=filter(lambda x:x["is_parent"]==True, data)
    if cid:
        for i in cid:
            sub_data=item_cats_get(i["cid"])
            if sub_data:
                add_item_cats(sub_data)
                temp(sub_data)


def topats_result_get(task_id):
    req = TopatsResultGetRequest(top.domain(0))
    req.set_app_info(top.appinfo(top.appkey(),top.secret(1)))

    req.task_id=task_id

    try:
        response = req.getResponse()
        return response
    except Exception,e:
        print e    

def topats_itemcats_get(cid,format="csv"):
    req = TopatsItemcatsGetRequest(top.domain(1))
    req.set_app_info(top.appinfo(top.appkey(),top.secret(1) ))

    req.cids=cid
    req.output_format=format

    try:
        response = req.getResponse()
        return response
    except Exception,e:
        print e