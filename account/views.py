#-*- coding:utf-8 -*-
import json
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
from account.models import Account

def default(request):
    """
    """
    return render_to_response('account/default.html',context_instance=RequestContext(request))

def detail(request,user_id):
	return render_to_response('account/account.html',context_instance=RequestContext(request))

@csrf_exempt
def register(request):
	"""
	用户注册
	ajax(post): ajax提交注册,返回JSON数据;
	http get: 返回register html页面;
	http post: 用户Form提交注册, 
	"""
	if request.is_ajax():
		email = request.POST.get("email")
		pwd = request.POST.get("pwd")
		nickname = request.POST.get("nickname")
		msg = ""
		result =""
		if not email:
			msg ="请输入邮箱"
		if not pwd:
			msg += "\n 请输入密码"
		if not nickname:
			msg += "\n 请设置昵称"
		try:
			acc = Account.objects.register_account(nickname,email,pwd)
		except Exception, e:
			result = "error"
			msg = e
		else:
			result ="success"
		finally:
			pass
		data =json.dumps(dict(result=result,msg=msg),separators=(',',':'))
		return HttpResponse(data,mimetype="appliction/json")
		
	else:
		if request.method=="GET":
			return render_to_response('account/register.html',context_instance=RequestContext(request))
		elif request.method=="POST":
			email = request.POST.get("email")
			pwd = request.POST.get("pwd")
			return render_to_response('account/register.html',context_instance=RequestContext(request))

def active(request):
	pass

def login(request):
	return render_to_response('account/login.html',context_instance=RequestContext(request))

def logout(request):
	pass

def checking(request):
	if request.is_ajax():
		tag = request.GET.get("type")
		if tag=="E":
			data = {"result":"success","status":"N"}
			js = json.dumps(data)
			return HttpResponse(js,mimetype='appliction/json')

