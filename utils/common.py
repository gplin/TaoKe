#-*- coding:utf-8 -*-
import os
from lxml import etree
from share.models import Category


def get_category(enable):
    """
    return list: dict in dict
    """
    li = []
    cate = list(Category.objects.filter(enable=enable).values('category_id','name','parent_id','enable','display_seq','add_up','is_hot','type'))
    for c in filter(lambda x:x['parent_id']==0,cate):
        c['items']=filter(lambda x:x['parent_id']==c['category_id'],cate)
        li.append(c)
    return li

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

        items = etree.SubElement(cate,"items")
        for i in e["items"]:
            item = etree.SubElement(items,"item")
            create_subElement(item,"name",i["name"])
            create_subElement(item,"id",i["category_id"])
            create_subElement(item,"seq",i["display_seq"])
            create_subElement(item,"ishot",i["is_hot"])

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


if __name__=="__main__":
    #li = get_Category(True)
    #print type(li)
    #gen_xml(li)
    #gen_html()

    pass
