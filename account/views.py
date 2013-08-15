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
from account.models import Account

def default(request):
    """
    """
    return render_to_response('account/default.html',context_instance=RequestContext(request))

def detail(request,user_id):
	return render_to_response('account/account.html',context_instance=RequestContext(request))

def register(request):
	pass

def active(request):
	pass

def login(request):
	return render_to_response('account/login.html',context_instance=RequestContext(request))

def logout(request):
	pass

def checking(request,tag):
	pass