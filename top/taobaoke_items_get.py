# -*- coding: utf-8 -*-
'''
Created on 2012-7-3
'''
from datetime import datetime
from uuid import uuid1
import urllib
import os
import sqlite3
from PIL import Image
import top.api


'''
这边可以设置一个默认的appkey和secret，当然也可以不设置
注意：默认的只需要设置一次就可以了
'''
top.setDefaultAppInfo("1021039194", "sandboxa7f002adf21ae4ec28f4fdb65")

'''
使用自定义的域名和端口（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com",80)

使用自定义的域名（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com")

使用默认的配置（调用线上环境）
a = top.api.UserGetRequest()

'''
a = top.api.TaobaokeItemsGetRequest("gw.api.tbsandbox.com")
a.pid = 30462502
#a.keyword = "女装,外套"
'''
可以在运行期替换掉默认的appkey和secret的设置
a.set_app_info(top.appinfo("appkey","*******"))
'''

a.fields="num_iid,title,nick,pic_url,price,click_url,commission,commission_rate,\
        commission_num,commission_volume,shop_click_url,seller_credit_score,item_location,volume"

 

def RequestItemData():
    """
    发出请求获取数据
    """
    for a.keyword in ['女装','男装','数码','家居','字画','电器','上衣']:
        print a.keyword
        f= a.getResponse()
        if f.has_key("Items_get_response"):
           res = f['Items_get_response']
           total_results = res["total_results"]
           #Data =[{},{}]
           data = res["Items"]["Item"]
           SaveToDB(data)
    
def SaveToDB(data):
    conn = sqlite3.connect("C:\workspace\git\TaoKe\db\TaoKe.db")
    c = conn.cursor()
    i=0
    for d in data:
        i = i+1
        #get the pic
        d_pic = downLoad_pic(d['pic_url'])

        orig_url =  None
        g_w =  None
        g_h =  None
        g_url =   None
        d_w =   None
        d_h =   None
        d_url =   None
        if len(d_pic)>0:
            orig_url =  d_pic[0]
            g_w =  d_pic[1]
            g_h =  d_pic[2]
            g_url =   d_pic[3]
            d_w =   d_pic[4]
            d_h =   d_pic[5]
            d_url =   d_pic[6]

        
        value =(d['volume'],d['nick'],d['click_url'],d['commission_rate'],
                 d['commission_num'],d['price'],d['seller_credit_score'],
                 d['num_iid'],d['item_location'],d['commission'],d['shop_click_url'],
                 d['commission_volume'],d['title'],d['pic_url'],datetime.now(),uuid1().get_hex(),
                 orig_url,d_w,d_h,d_url,g_w,g_h,g_url
                )

        c.execute("""Insert Into share_Item
        (account_id, category_id,add_up_love,add_up_bookmark,add_up_comment,
         volume, nick, click_url, commission_rate,
         commission_num,price,seller_credit_score,
         num_iid,location,commission,shop_click_url,
         commission_volume,
         title,
         pic_url,
         share_date,uuid,
         pic_url_orig,
         pic_width_detail,pic_height_detail,pic_url_detail,
         pic_width_grid,  pic_height_grid,  pic_url_grid
        )
        values(1,1002,0,0,0,
                ?,?,?,?,
                ?,?,?,
                ?,?,?,?,
                ?,?,?,?,?,
                ?,
                ?,?,?,
                ?,?,?)
        """,value)
        conn.commit()
        print "done %s" %i
    c.close()

def downLoad_pic(pic_url):
    try:
        #print pic_url
        g_size = 200,200
        d_size = 450,500
        
        #checking dir
        path = ["C:/workspace/git/TaoKe/media/img/o", 
                "C:/workspace/git/TaoKe/media/img/g", 
                "C:/workspace/git/TaoKe/media/img/d"]

        for p in path:
            if not os.path.exists(p):
                os.mkdir(p)
        #request pic
        pic_name = uuid1().get_hex()
        path_o = "%s/%s.jpg" % (path[0],pic_name)
        path_g = "%s/%s.jpg" % (path[1],pic_name)
        path_d = "%s/%s.jpg" % (path[2],pic_name)
        
        #print path_o
        urllib.urlretrieve(pic_url,path_o)
        
        img = Image.open(path_o)
        if img.mode!="RGB":
            img = img.convert("RGB")

        w,h = img.size
        #生成缩略图 w=450
        if w > d_size[0]:
            r = float(d_size[0])/float(w)
            new_size = (int(w*r),int(h*r))
            n = img.resize(new_size,Image.ANTIALIAS)
            n.save(path_d)
            d_size = n.size
        else:
            img.save(path_d)
            d_size = img.size

        #生成缩略图 w=200
        if w > g_size[0]:
            r = float(g_size[0])/float(w)
            new_size = (int(w*r),int(h*r))
            n = img.resize(new_size,Image.ANTIALIAS)
            n.save(path_g)
            g_size = n.size
        else:
            img.save(path_g)
            g_size = img.size

        print "img download done"
        return [path_o[23:],g_size[0],g_size[1],path_g[23:],d_size[0],d_size[1],path_d[23:]]
    except Exception,e:
        print "error:",(e)
        pass
        return []
        


if __name__=="__main__":
    RequestItemData()
    

