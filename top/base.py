#-*- coding:utf-8 -*-
# desc: top API base function
import urllib
import sqlite3
import os
from uuid import uuid1
from PIL import Image
from django.conf import settings


def downLoad_item_pic(pic_url):
    try:
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

        return dict(pic_url_orig=path_o[23:],
                    pic_width_grid=g_size[0],
                    pic_height_grid=g_size[1],
                    pic_url_grid=path_g[23:],
                    pic_width_detail=d_size[0],
                    pic_height_detail=d_size[1],
                    pic_url_detail=path_d[23:],
                    uuid=pic_name
                   )
    except Exception,e:
        print e
        return None
