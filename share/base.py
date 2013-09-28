#-*- coding:utf-8 -*-

from top.base import downLoad_item_pic
from top.taobaoke_items_detail_get import extract_num_iid,get_detail
from share.models import Item


def item_save(account_id,url):
    ""
    num_iids = extract_num_iid(url)
    for id in num_iids:
        data=get_detail(id)
        for item in data:
            pic=downLoad_item_pic(item["item"]["pic_url"])
            temp=Item.objects.save_item_from_detail_get(account_id=account_id,data=item,pic=pic)
            return temp
    return None


