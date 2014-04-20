#-*- coding:utf-8 -*-
from django.conf.urls import patterns,url

from master import views

urlpatterns = patterns('',
    url(r'^$',views.master,name='master'),
)
