#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext


def master(request):
    return render_to_response('admin/common.html',context_instance=RequestContext(request))