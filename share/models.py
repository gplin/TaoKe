#-*- coding:utf-8 -*-
from django.db import models

class Taobaoke_Item(models.Model):
    rec_num = models.IntegerField(primary_key=True,unique=True)
    num_iid = models.CharField(max_length=50)
    seller_id = models.CharField(max_length=50,null=True)
    nick = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20,decimal_places=6)
    item_location = models.CharField(max_length=100)
    seller_credit_score = models.DecimalField(max_digits=10,decimal_places=0)
    click_url = models.CharField(max_length=500)
    shop_click_url = models.CharField(max_length=500)
    pic_url = models.CharField(max_length=500)
    taobaoke_cat_click_url = models.CharField(max_length=500,null=True)
    keyword_click_url = models.CharField(max_length=500,null=True)
    coupon_rate = models.CharField(max_length=50,null=True)
    coupon_price = models.DecimalField(max_digits=20,decimal_places=6,null=True)
    coupon_start_time = models.CharField(max_length=20,null=True)
    coupon_end_time = models.CharField(max_length=20,null=True)
    commission_rate = models.CharField(max_length=20)
    commission = models.DecimalField(max_digits=20,decimal_places=6)
    commission_num = models.CharField(max_length=20)
    commission_volume = models.DecimalField(max_digits=20,decimal_places=0)
    shop_type = models.CharField(max_length=5,null=True)
    volume = models.DecimalField(max_digits=30,decimal_places=2)
    #customer column
    pic_width_first = models.IntegerField(null=True)
    pic_height_first = models.IntegerField(null=True)
    pic_local_url_first = models.CharField(max_length=250,null=True)
    pic_width_second = models.IntegerField(null=True)
    pic_height_second = models.IntegerField(null=True)
    pic_local_url_second = models.CharField(max_length=250,null=True)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


