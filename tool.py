#-*- coding:utf-8 -*-
import urllib
import sqlite3
import uuid
from PIL import Image



def main():
    """
    根据pic_url下载并保存图片
    """
    conn = sqlite3.connect("db\mysite.db")
    c = conn.cursor()
    cur = conn.cursor()
    c.execute("""select rec_num, pic_url from share_taobaoke_item where rec_num>157 """)
    w_1st = 500
    w_2nd = 200
    st_size = 500,500
    nd_size = 200,200
    for row in c:
        #get the pictue
        url = row[1]
        print row[0],url
        #原始图片
        raw_path ="media\img\%s" % url.split("/")[-1]
        data = urllib.urlretrieve(url,raw_path)
        img = Image.open(raw_path)
        print img.mode
        if img.mode != "RGB":
            img =img.convert("RGB")
        w,h = img.size
        print img.mode
        name = uuid.uuid1().hex
        path_1st = "media/img/1st/%s.jpg" % name 
        path_2nd = "media/img/2nd/%s.jpg" % name

        print raw_path
        print path_1st
        print path_2nd
        #1st: w=500,缩略图
        if w > w_1st :
            r = float(w_1st)/float(w)
            new_size = (int(w*r),int(h*r))
            n = img.resize(new_size,Image.ANTIALIAS)
            n.save(path_1st)
            st_size = n.size
        else:
            img.save(path_1st)
            st_size = img.size
        #2nd :w=200, 缩略图  
        if w > w_2nd :
            r = float(w_2nd)/float(w)
            new_size = (int(w*r),int(h*r))
            n = img.resize(new_size,Image.ANTIALIAS)
            n.save(path_2nd)
            nd_size = n.size
        else:
            img.save(path_2nd)
            nd_size = img.size
        print row[0],img.size,st_size,nd_size
        #update db
                    
        cur.execute("""Update
                            share_taobaoke_item
                       Set
                            pic_width_first =?,
                            pic_height_first =?,
                            pic_local_url_first =?,
                        
                            pic_width_second = ?,
                            pic_height_second =?,
                            pic_local_url_second =?
                       Where rec_num = ? """,(st_size[0],st_size[1],path_1st,nd_size[0],nd_size[1],path_2nd,row[0])
                    )
        conn.commit()
        print "update rec_num %s" % row[0]
    conn.close()    


if __name__ == "__main__":
    main()
