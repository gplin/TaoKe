#-*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django import forms

from account.models import Account


class RegisterForm(forms.Form):
    """
    """
    email = forms.EmailField(label=u'电子邮箱',required=True,
                                error_messages={'required':u'请输入电子邮箱','invalid':u'邮箱格式有误'}
                                )
    username = forms.CharField(label=u'昵称',required=True,max_length=20,
                                error_messages={'required':u'请设置昵称',
                                                'invalid':u'昵称长度不能超过20'}
                                )
    password = forms.CharField(label=u'设置密码',widget = forms.PasswordInput(render_value=False),
                                required=True,max_length=20,min_length=6,
                                error_messages={'required':u'请输入密码,6-20位',
                                                'invalid':u'请设置密码字符为6-20位字符(数字或字母)'}
                                )
    confirm_password = forms.CharField(label=u'确认密码',widget = forms.PasswordInput(render_value=False),
                                required=True,max_length=20,min_length=6,
                                error_messages={'required':u'请再次输入密码',
                                                'invalid':u'请设置密码字符为6-20位字符(数字或字母)'}
                                )

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

    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError(u"两次输入的密码不一致")
        return self.cleaned_data