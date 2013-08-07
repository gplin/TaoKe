#-*- coding:utf-8 -*-
from django.conf.urls import patterns,url
from django.views.generic import DetailView, ListView
from share import views

urlpatterns = patterns('',
    url(r'^$',views.default,name='default'),
    url(r'^(?P<item_id>\d{1,15})/$',views.detail,name="detail"),
    url(r'^c/(?P<category_id>\d{4})/(?P<page>\d{1,5})/$', views.get_item_by_category_id, name="c"),
    url(r'^(?P<uuid>[A-Za-z0-9]{32})/$',views.goto_taobao,name='goto_taobao'), 
    url(r'^JSON/(?P<page>.*$)$',views.JSON,name='JSON'),
    url(r'^gen/$',views.execute_generate_menu,name='execute_generate_menu'),
)












































