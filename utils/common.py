#-*- coding:utf-8 -*-
import os
import urllib
from uuid import uuid1
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

from lxml import etree
from PIL import Image

from share.models import Item_Cats

def create_subElement(root,subElementName,subElementText):
    """
    添加子节点
    """
    element = etree.SubElement(root,subElementName)
    element.text = unicode(subElementText)

def generate_xml(elements):
    root = etree.Element("categories")
    for e in elements:
        if e['type']==Category.CLOTHES:
            cate = etree.SubElement(root,"clothes")
        else:
            cate = etree.SubElement(root,"category")
        
        create_subElement(cate,"name",e["name"])
        create_subElement(cate,"id",e["category_id"])
        create_subElement(cate,"seq",e["display_seq"])
        create_subElement(cate,"type",e["type"].lower())

        items = etree.SubElement(cate,"items")
        for i in e["items"]:
            item = etree.SubElement(items,"item")
            create_subElement(item,"name",i["name"])
            create_subElement(item,"id",i["category_id"])
            create_subElement(item,"seq",i["display_seq"])
            create_subElement(item,"ishot",i["is_hot"])
            create_subElement(item,"type",e["type"].lower())

    return etree.tostring(root,encoding='utf-8')

def generate_menu(data,xmlPath,xslPath,menuPath):
    """
    生成MENU
    """
    # 1.获取菜单、类目
    # 2.生成xml(文件)
    # 3.生成menu.html
    xml = generate_xml(data)
    with open(xmlPath,'w') as f:
        f.write(xml)
    xsltDoc = etree.parse(xslPath)
    xmlDoc  = etree.parse(xmlPath)
    transform = etree.XSLT(xsltDoc)
    result = transform(xmlDoc)
    result.write_c14n(menuPath)

def send_register_email(uuid,to_email):
    subject= "亲! 注册激活"
    body = """亲,欢迎注册**网, 请点下面链接激活账号吧:<a href='http://127.0.0.1:8000/account/active/%s/'><b>点击此处立即激活账号</b></a>
                <p>如果上面链接无法打开,请复制以下链接至浏览器:</br>
                http://127.0.0.1:8000/account/active/%s/</p>""" % (uuid, uuid)
    msg =  EmailMessage(subject,body,settings.EMAIL_HOST_USER,[to_email])
    msg.content_subtype = 'html' #Main content is now text/html
    msg.send()

# if __name__=="__main__":
#     #li = get_Category(True)
#     #print type(li)
#     #gen_xml(li)
#     #gen_html()

#     pass

def downLoad_pic(pic_url):
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

        # print "img download done"
        # return [path_o[23:],g_size[0],g_size[1],path_g[23:],d_size[0],d_size[1],path_d[23:]]
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