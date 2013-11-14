#-*- coding:utf-8 -*-
from django.conf.urls import patterns,url
from django.views.generic import DetailView, ListView
from share import views

urlpatterns = patterns('',
    url(r'^(?P<cats>(df|cl|sh|ba|ac|ho|cr|co))$',views.share,name="cats"),
    # url(r'^$',views.share,name='share'),
    url(r'^dat$',views.data,name='dat'),
    url(r'^(?P<item_id>\d{1,15})/$',views.detail,name="detail"),
    url(r'^(?P<user_id>\d{1,15})/(?P<type>(default|love|album|follow))$',views.get_item_by_account,name='acc_detail'),

    # 
    # share item 
    url(r'^action/$',views.get_share_item_from_taobao,name="action"),
    #go to taobao site
    url(r'^(?P<uuid>[A-Za-z0-9]{32})/$',views.goto_taobao,name='goto_taobao'), 
    #utils
    url(r'^gen/$',views.execute_generate_menu,name='execute_generate_menu'),

)












































