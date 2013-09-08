#-*- coding:utf-8 -*-
import json
from django.utils import simplejson
from django.db.models.query import QuerySet
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render,get_object_or_404
from django.core.urlresolvers import reverse
from django.core import exceptions
from django.core.serializers import serialize,deserialize
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.conf import settings

# import Taoke.settings
from utils.common import send_register_email
from account.models import Account
from share.models import Taobaoke_Item,Item_Love
from account.form import RegisterForm


def default(request):
    """
    """
    return render_to_response('account/default.html',context_instance=RequestContext(request))

def detail(request,user_id):
    return render_to_response('account/account.html',context_instance=RequestContext(request))

@never_cache
@csrf_exempt
# @transaction.commit_manually
@transaction.commit_on_success
def register(request):
    """
    用户注册
    ajax(post): ajax提交注册,返回JSON数据;
    http get: 返回register html页面;
    http post: 用户Form提交注册, 
    """
    response = ""
    if request.is_ajax():
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        nickname = request.POST.get("username")
        msg = []
        result =""
        uuid =""
        
        # checking
        try:
            if not email:
                msg.append("请输入邮箱")
            if not pwd:
                msg.append("请输入密码")
            if not nickname:
                msg.append("请设置昵称")
            if len(msg)>0:
                raise Exception
        
            acc = Account.objects.register_account(nickname,email,pwd)
            result="success"
            uuid=acc.uuid
        except Exception,e:
            result = "error"
            data =json.dumps(dict(result=result,msg=msg,email=email),separators=(',',':'))
            response=HttpResponse(data,mimetype="appliction/json")

            # transaction.rollback()
        else:
            send_register_email(uuid, email)
            data =json.dumps(dict(result=result,msg=msg,email=email),separators=(',',':'))
            response=HttpResponse(data,mimetype="appliction/json")

            # transaction.commit()
        
        # return response
    else:
        if request.method=="GET":
            response = render_to_response('account/register.html',{"form":RegisterForm(auto_id=True)},
                                        context_instance=RequestContext(request))
        elif request.method=="POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                username = form.cleaned_data["username"]
                acc = Account.objects.register_account(username, email, password)

                response = render_to_response('account/register.html',{"registed":"Y","email":email},
                                            context_instance=RequestContext(request))
            else:
                response = render_to_response('account/register.html',{"form":form},
                                            context_instance=RequestContext(request))
        # transaction.commit()
    return response

def active(request,license):
    u"""
        parameter
            uuid:  
    用户账号激活 
    注: 已激活账号直接转向登录页面
    """
    try:
        acc = Account.objects.active_account(license)
    except Exception, e:
        # log
        return HttpResponseRedirect('/account/login/')

    return render_to_response('account/active.html',{"username":acc.user.username},context_instance=RequestContext(request))
    
    
@never_cache
@csrf_exempt
def login(request):
    u"""
     用户登录:
     1.已登录用户重定向到我的首页
     2.未登录用户则验证
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect("/share/")
    if request.is_ajax():
        try:
            msg = []
            # e=""
            login_id = request.POST["login_id"]
            password = request.POST["password"]
            if not login_id:
                msg.append("请输入登录帐号(邮箱或昵称)")
            if not password:
                msg.append("请输入登录密码")
            if msg:
                raise Exception
            
            user = authenticate(username=login_id,password=password) or authenticate(email=login_id,password=password)
            if user is not None:
                if user.is_active:
                    # return HttpResponseRedirect('/share/')
                    auth_login(request,user)
                    data =json.dumps(dict(result="success",msg=user.username),separators=(',',':'))
                    return HttpResponse(data,mimetype="appliction/json")
                else:
                    msg.append("帐号未激活.")
                    raise Exception
            else:
                msg.append("登录账号或密码有误.")
                raise Exception
        except Exception, e:
            data =json.dumps(dict(result="error",msg=msg),separators=(',',':'))
            return HttpResponse(data,mimetype="appliction/json")
        else:
            return HttpResponseRedirect('/share/')
    else:
        if request.method=="GET":
            return render_to_response('account/login.html',context_instance=RequestContext(request))
        elif request.method=="POST":
            # TODO: login in
            return render_to_response('account/login.html',context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/share/")

def checking(request):
    u"""
     检查邮箱或用户名是否已被注册
    """
    if request.is_ajax():
        tag = request.GET.get("type")
        value = request.GET.get("value")
        flag = Account.objects.check_account_exists(tag,value)
        data = dict(result="success",status="Y" if flag else "N")
        js = json.dumps(data,separators=(',',':'))
        return HttpResponse(js,mimetype='appliction/json')

@csrf_exempt
@never_cache
def love(request):
    """
    用户添加喜爱商品
    """
    if not request.user.is_authenticated():
        return HttpResponse(json.dumps(dict(result='error',logined='N'),separators=(',',':')),mimetype='appliction/json')
    elif request.user.is_authenticated():
        if request.is_ajax():
            data = ""
            try:
                user_id = request.user.id
                item_id = request.POST["item_id"]
                Item_Love.objects.set_item_love(item_id,user_id)
                data = json.dumps(dict(result='success',user_id=user_id,item_id=item_id),separators=(',',':'))
            except Exception, e:
                # TODO : log
                data = json.dumps(dict(result='error'),separators=(',',':'))
            
            return HttpResponse(data,mimetype='appliction/json')

