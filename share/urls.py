#-*- coding:utf-8 -*-
from django.conf.urls import patterns,url
from django.views.generic import DetailView, ListView
from share import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^JSON/(?P<page>.*$)$',views.JSON,name='JSON'),
    url(r'^Demo1/$',views.Demo1,name='Demo1'),
)












































