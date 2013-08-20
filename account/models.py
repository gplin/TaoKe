#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User,UserManager


class AccountManager(models.Manager):
	"""
	"""
	def new_account(self,email):
		pass

class Account(models.Model):
    user = models.OneToOneField(User,primary_key=True,db_column="user_id")
    add_up_onLine_time = models.TimeField(editable=False,auto_now_add=True)
    icon = models.ImageField(upload_to='Icon/%Y/%m',blank=True,help_text ='用户头像')
    about = models.TextField(blank=True,help_text='关于用户的标签')
    grade = models.IntegerField(default=0,editable=False,help_text='用户积分')
    uuid = models.CharField(unique=True,editable=False,max_length=32)
    add_up_item = models.IntegerField(default=0)