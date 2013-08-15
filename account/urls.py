#-*- coding:utf-8 -*-
# author: gplin
# date: 2013-08-11

from django.conf.urls import url,patterns
from account import views

urlpatterns = patterns('',
    url(r'^$',views.default,name='default'),
    url(r'^(?P<user_id>\d{1,15})/$',views.detail,name='account'),
    #用户:注册->发送邮件验证->激活->登录->退出
    url(r'^register/$',views.register,name='register'),
    url(r'^active/(?P<license>[A-Za-z0-9]{32})/$',views.active,name='active'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    #用户注册时邮件校验及用户信息设置时的相关校验
    url(r'^checking/(?P<tag>(email|nickname))/$',views.checking,name='checking'),
)