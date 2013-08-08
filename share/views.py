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
from share.models import Taobaoke_Item,Category
from utils.common import generate_menu

def default(request):
    """
    """
    return render_to_response('share/default.html',context_instance=RequestContext(request))

def detail(request,item_id):
    """
    根据参数[rec_num],查询宝贝详细信息
    """
    model = Taobaoke_Item.objects.select_related().get(item_id=item_id)
    item_u = Taobaoke_Item.objects.get_relate_by_user_id(model.user.user_id,1)

    return render_to_response('share/detail.html',
                               {"model":model,"relate_u":item_u},
                               context_instance=RequestContext(request))

def get_item_by_category_id(request,category_id,page):
    """
    根据分类ID参数获取宝贝信息,ajax 请求返回JSON格式
    """
    page = page if page else 1
    if request.is_ajax():
        json = Taobaoke_Item.objects.get_relate_by_category_id(category_id,page)
        return HttpResponse(json,mimetype='appliction/json')

def get_item_by_category_type(request,type,page=None):
    """
    获取分类宝贝
    """
    if request.is_ajax():
        json = Taobaoke_Item.objects.get_item_by_category_type(type,page)
        return HttpResponse(json,mimetype='appliction/json')
    else:
        if request.method == 'GET':
            return render_to_response('share/category.html',context_instance=RequestContext(request))

def goto_taobao(request,uuid):
    """跳转到淘宝"""
    model = get_object_or_404(Taobaoke_Item,uuid = uuid)
    return render_to_response("share/2taobao.html",{"taobao_url":model.click_url})

def JSON(request,page):
    page = page if page else 1
    if request.is_ajax():
        json = Taobaoke_Item.objects.get_share_item_json(page,20)
        return HttpResponse(json,mimetype='application/json')


# @csrf_exempt

def execute_generate_menu(request):
    import os
    xmlPath = os.path.join(settings.GENERATE_TEMPLATE_DIR,'menu.xml')
    xslPath = os.path.join(settings.GENERATE_TEMPLATE_DIR,'menu.xsl')
    menuPath = os.path.join(settings.GENERATE_TEMPLATE_DIR,'menu.html')
    generate_menu(Category.objects.get_category_tree(True),xmlPath,xslPath,menuPath)
    return HttpResponse("generate menu done: "+menuPath)