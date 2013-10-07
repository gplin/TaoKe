#-*- coding:utf-8 -*-
from django.conf.urls import patterns,url
from django.views.generic import DetailView, ListView
from share import views

urlpatterns = patterns('',
    url(r'^$',views.share,name='share'),
    url(r'^(?P<item_id>\d{1,15})/$',views.detail,name="detail"),
    url(r'^(?P<type>(cl|sh|ba|ac|ho|cr|co))/$',views.get_by_category_type,name="category"),
    # url(r'^(?P<type>(cl|sh|ba|ac|ho|cr|co))/(?P<category_id>\d{4})/$',views.get_by_category_type,name="category_id"),
    # 
    url(r'^cats/(?P<cid>\d{1,15})/$',views.get_relate_by_cid,name="get_relate_by_cid"),
    # share item 
    url(r'^action/$',views.get_share_item_from_taobao,name="action"),
    #go to taobao site
    url(r'^(?P<uuid>[A-Za-z0-9]{32})/$',views.goto_taobao,name='goto_taobao'), 
    #utils
    url(r'^gen/$',views.execute_generate_menu,name='execute_generate_menu'),

)












































