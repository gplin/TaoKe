#-*- coding:utf-8 -*-
import urllib
import sqlite3
import uuid
import os
from PIL import Image



def main():
    """
    根据pic_url下载并保存图片
    """
    conn = sqlite3.connect("db\Taoke.db")
    c = conn.cursor()
    conn2 = sqlite3.connect("db\Taoke.db")
    cur = conn2.cursor()
    c.execute("""select item_id, pic_url from share_Item where item_id=1 order by item_id asc """)
    w_1st = 500
    w_2nd = 200
    st_size = 450,500
    nd_size = 200,200
    for row in c:
        if not os.path.exists("media\img\o"):
            os.mkdir("media\img\o")
        if not os.path.exists("media\img\g"):
            os.mkdir("media\img\g")
        if not os.path.exists("media\img\d"):
            os.mkdir("media\img\d")
            
        print row[0]
        #get the pictue
        url = row[1]
        #print row[0],url
        #原始图片
        raw_path ="c:/workspace/git/taoke/media/img/%s" % uuid.uuid1().get_hex() +".jpg"
        print raw_path
        data = urllib.urlretrieve(url,raw_path)
        img = Image.open(raw_path)
        #print img.mode
        if img.mode != "RGB":
            img =img.convert("RGB")
        w,h = img.size
        #print img.mode
        name = uuid.uuid1().get_hex()
        path_orig = "media/img/o/%s.jpg" % name
        path_1st = "media/img/d/%s.jpg" % name 
        path_2nd = "media/img/g/%s.jpg" % name

        img.save(path_orig)
        
        
        #print raw_path
        #print path_1st
        #print path_2nd
        #1st: w=450,缩略图
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
        #print row[0],img.size,st_size,nd_size
        #update db
        #img.close()
        #print path_orig
        #print "c:/workspace/git/taoke/"+path_orig
        #os.rename(raw_path,"c:/workspace/git/taoke/"+path_orig)
                    
        cur.execute("""Update
                            share_Item
                       Set
                            pic_width_detail =?,
                            pic_height_detail =?,
                            pic_url_detail =?,
                        
                            pic_width_grid = ?,
                            pic_height_grid =?,
                            pic_url_grid =?,

                            pic_url_orig=?
                       Where item_id = ? """,(st_size[0],st_size[1],path_1st,nd_size[0],nd_size[1],path_2nd,path_orig,row[0])
                    )
        conn2.commit()
        print "update rec_num %s" % row[0]
    conn.close()
    conn2.close()

def UpdateUUID():
    conn = sqlite3.connect("db\Taoke.db")
    c = conn.cursor()
    c.execute("""Update share_Item Set pic_width_detail=null, pic_height_detail=null, pic_url_detail=null
                            ,pic_width_grid=null
                            ,pic_height_grid=null
                            ,pic_url_grid=null
                            ,pic_url_orig=null
                    """ )
    conn.commit()
    print "Updated "
    conn.close()

    
if __name__ == "__main__":
    main()
    #UpdateUUID()
