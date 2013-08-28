#-*- coding:utf-8 -*-
import uuid
import json
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User,UserManager


class AccountManager(models.Manager):
    """
    """
    def create_account(self,username,email,password):
        user = User.objects.create_user(username, email, password)
        user.is_active = False
        user.save()

        acc =  self.model(user=user,icon=settings.ACCOUNT_DEFAULT_ICON,uuid=uuid.uuid1().hex)
        acc.save()
        return acc

    def register_account(self,nickname,email,password):
       return self.create_account(username=nickname,email=email,password=password)
         

    def active_account(self,uuid):
        """
        激活帐号
        """
        acc = self.select_related().get(uuid=uuid)
        if acc.user.is_active:
            raise ObjectDoesNotExist

        from django.db import connection,transaction
        cursor = connection.cursor()
        cursor.execute("""Update auth_user 
                          Set is_active = %s 
                          Where exists (Select * From account_account acc 
                                         Where auth_user.id = acc.user_id
                                         and acc.uuid = %s)
                          and auth_user.is_active = %s
                          """,[True,uuid,False])
        transaction.commit_unless_managed()
        data = dict(result="success",data=dict(username=acc.user.username,email=acc.user.email))
        return json.dumps(data,separators=(',',':'))

    def check_account_exists(self,type,value):
        """
        校验Email,nickname是否存在
        parameter
                type: E -> Email,N -> Nickname
        return  boolean
        """
        type = type if type.strip().upper() else None
        value = value if value.strip() else None
        if type is None or type not in("E","N") or value is None:
            raise ValueError("type and value can not empty.")
        try:
            user = User.objects.get(email=value) if type=="E" else User.objects.get(username=value)
            self.select_related().get(user=user)
        except ObjectDoesNotExist:
            return False
        except Exception:
            raise
        
        return True



class Account(models.Model):
    user = models.OneToOneField(User,primary_key=True,db_column="user_id")
    add_up_onLine_time = models.TimeField(editable=False,auto_now_add=True)
    icon = models.ImageField(upload_to='Icon/%Y/%m',blank=True,help_text ='用户头像')
    about = models.TextField(blank=True,help_text='关于用户的标签')
    grade = models.IntegerField(default=0,editable=False,help_text='用户积分')
    uuid = models.CharField(unique=True,editable=False,max_length=32)
    add_up_item = models.IntegerField(default=0)

    objects = AccountManager()

    def __unicode__(self):
        return unicode('%s:%s' %(self.user.username,self.user.email))

    def __str__(self):
        return self.__unicode__()