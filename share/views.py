#-*- coding:utf-8 -*-
from django.utils import simplejson
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render,get_object_or_404
from django.core.urlresolvers import reverse
from django.core.serializers import serialize,deserialize
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.conf import settings

# import Taoke.settings
from share.models import Item,Item_Cats
from share.base import item_save
from utils.common import generate_menu
from utils.taoke_json import dict2JSON

ResponeType='appliction/json'

def JSON_HttpResponse(json):
    return HttpResponse(json,mimetype=ResponeType)

def json(request):
    if request.is_ajax():
        page = request.GET.get("page")
        cats = request.GET.get("cats")
        cid = request.GET.get("cid")
        user_id = request.user.id if request.user.is_authenticated() else None
        return JSON_HttpResponse(Item.objects.get_item_data(page=page,user_id=user_id,cats=cats,cid=cid))

def share(request):
    """
    """
    return render_to_response('share/main.html',context_instance=RequestContext(request))

def get_by_cats(request):
    """
    获取分类宝贝
    """
    return render_to_response('share/%s.html' % type,context_instance=RequestContext(request))

def get_relate_by_cid(request,cid):
    if request.is_ajax():
        page = request.GET.get('page')
        user_id = request.user.id if request.user.is_authenticated() else None
        data = Item.objects.get_item_by_category(user_id,None,cid,page)
        return JSON_HttpResponse(data)

def get_item_by_account(request,user_id,type):
    u"""
    acc_id=user_id
    type:default; album; love; follow;
    """
    if request.is_ajax():
        page=request.GET.get("page")
        page=page if page else 1
        data=Item.objects.get_item_by_account(user_id,type,page)
        return JSON_HttpResponse(data)



def detail(request,item_id):
    """
    根据参数[rec_num],查询宝贝详细信息
    """
    model = Item.objects.select_related().get(item_id=item_id)
    # item_u = Item.objects.get_relate_by_user_id(model.user.user_id,1)

    return render_to_response('share/detail.html',
                               {"model":model,"relate_u":None},
                               context_instance=RequestContext(request))

@csrf_exempt
def get_share_item_from_taobao(request):
    u"""
    根据分享链接获取分享的宝贝信息:
    """
    if request.is_ajax() and request.user.is_authenticated():
        account_id=request.user.id
        url=request.POST.get("url")
        p=request.POST.get("p")
        item_id=request.POST.get("item_id")
        comment=request.POST.get("comment")
        if p and item_id:
            # active and update comment item
            item=Item.objects.update_comment_active(item_id,comment)
        elif url:
            # get item from taobao 
            item=item_save(account_id, url)
        return JSON_HttpResponse(item.serializers_to_json())


def goto_taobao(request,uuid):
    """跳转到淘宝"""
    model = get_object_or_404(Item,uuid = uuid)
    return render_to_response("share/2taobao.html",{"taobao_url":model.click_url})



# @csrf_exempt
#utils method
def execute_generate_menu(request):
    import os
    xmlPath = os.path.join(settings.UTILS_TEMPLATE_DIR,'menu.xml')
    xslPath = os.path.join(settings.UTILS_TEMPLATE_DIR,'menu.xsl')
    menuPath = os.path.join(settings.INCLUDES_TEMPLATE_DIR,'menu.html')
    generate_menu(Category.objects.get_category_tree(True),xmlPath,xslPath,menuPath)
    return HttpResponse("generate menu done: "+menuPath)