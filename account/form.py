#-*- coding:utf-8 -*-
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms

from account.models import Account


class RegisterForm(forms.Form):
    """
    """
    pwd_error_msg = {'required':  u'请输入密码,6-20位(数字或字母)',
                     'invalid':   u'请设置密码字符为6-20位字符(数字或字母)',
                     'max_length':u'请设置密码字符为6-20位字符(数字或字母)',
                     'min_length':u'请设置密码字符为6-20位字符(数字或字母)'
                     }

    email = forms.EmailField(label=u'电子邮箱',required=True,
                                error_messages={'required':u'请输入电子邮箱','invalid':u'邮箱格式有误'})
    username = forms.CharField(label=u'昵称',required=True,max_length=20,
                                error_messages={'required':u'请设置昵称',
                                                'invalid':u'昵称长度不能超过20'})
    password = forms.CharField(label=u'设置密码',widget=forms.PasswordInput(),
                                required=True,max_length=20,min_length=6,
                                error_messages=pwd_error_msg)
                                                                # render_value=False
    confirm_password = forms.CharField(label=u'确认密码',widget=forms.PasswordInput(),
                                      max_length=20,required=True,
                                      error_messages={'required':'请输入确认密码6-20位(数字或字母)'})

    def clean_email(self):
        email = self.cleaned_data['email']
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError(u" 邮箱已被注册")
        return email

    def clean_username(self):
        name = self.cleaned_data['username']
        is_exists = User.objects.filter(username=name).exists()
        if is_exists:
            raise forms.ValidationError(u"昵称已被占用")
        return name

    def clean_password(self):
        u"""
        校验密码,只能为数字或字母组成.
        """
        pwd = self.cleaned_data['password']
        if re.findall(r"[^0-9A-Za-z]", pwd, re.I):
            raise forms.ValidationError(u'密码只能为数字或字母')
        return pwd

    def clean_confirm_password(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError(u"两次输入的密码不一致")
        return self.cleaned_data['confirm_password']


class InfoForm(forms.Form):
    u"""
    用户基本信息
    """
    email=forms.EmailField(label=u'注册邮箱',required=True)
    username=forms.CharField(label=u'昵称',required=True,max_length=20)