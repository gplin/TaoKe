#-*- coding:utf-8 -*-

from top.taobaoke_items_detail_get import extract_num_iid,get_detail


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
            pic=downLoad_pic(item["item"]["pic_url"])
            temp=Item.objects.save_item_from_detail_get(account_id=1,data=item,pic=pic)
            print "done %s" % temp.num_iid

    print "done test share"