#-*- coding:utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.serializers import serialize,deserialize
from account.models import Account

class Category(models.Model):
    """
    宝贝类别: 衣服；包包；家居
    """
    category_id = models.AutoField(primary_key=True,null=False,unique=True)
    name = models.CharField(max_length=20,blank=False,unique=True,help_text='分类名称')
    parent_id = models.IntegerField(default=0)
    enable = models.BooleanField(default=True)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)
    display_seq =models.IntegerField(default=0)
    add_up = models.IntegerField(default=0)
    is_hot= models.BooleanField(default=False)

    class Meta():
        ordering = ['display_seq','enable','init_date','name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Style(models.Model):
    '''
          风格名称，如复古，怀久
    '''
    style_id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=20,unique=True,blank=False,help_text='风格名称,eg:复古')
    enable = models.BooleanField(default=True)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)
    add_up = models.IntegerField(default=0)
    is_hot= models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
    
    class Meta():
        ordering = ['name','-init_date'] 


class PopularElement(models.Model):
    '''
    流行元素
    '''
    popular_element_id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=50,unique=True,help_text='流行元素,eg:情侣')
    enable = models.BooleanField(default=True)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)
    add_up = models.IntegerField(default=0)

    class Meta():
        ordering = ['name','-init_date']
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    '''
    商品品牌
    '''
    brand_id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=50,unique=True,help_text='品牌')
    enable = models.BooleanField(default=True)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)
    add_up = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
    
    class Meta():
        ordering = ['name','-init_date']


class Color(models.Model):
    '''
    颜色
    '''
    color_id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=50,unique=True,help_text='颜色')
    enable = models.BooleanField(default=True)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)
    add_up = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
    
    class Meta():
        ordering = ['name','-init_date']
    

class Occasion(models.Model):
    '''
    场合
    '''
    occasion_id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=50,unique=True,help_text='场合')
    enable = models.BooleanField(default=True)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)
    add_up = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    
    class Meta():
        ordering = ['name','-init_date']

# 需要格式化输出的字段
JSON = 'json'
fields = ('item_id','title','price','pic_url_grid','pic_width_grid','pic_height_grid','add_up_love',
                'add_up_comment','desc')

class Taobaoke_Item_Manager(models.Manager):
    """
    """
    def get_share_grid(self,page,page_size=20):
        """
        """
        page = page if page else 1
        item =self.raw('''  Select item_id,title,price,
                                   pic_url_grid,pic_width_grid,pic_height_grid,
                                   add_up_love, add_up_comment, desc
                            From share_taobaoke_item
                            Order by add_up_love desc, add_up_bookmark desc, add_up_comment desc
                            Limit %s * (%s-1) ,%s ''',[page_size,page,page_size])

        return item

    def get_share_item_json(self,page,page_size=20):
        """
        返回JSON格式
        """
        fields = ('item_id','title','price','pic_url_grid','pic_width_grid','pic_height_grid','add_up_love',
                'add_up_comment','desc')
        item = self.get_share_grid(page,page_size)
        return serialize(JSON,item,fields=fields)

    def get_relate_by_category_id(self,category_id,page,page_size=20):
        """
        根据分类ID,页码,获取分享的宝贝
        """
        item = self.raw('''Select item_id,title,
                                           price,
                                           pic_url_grid,
                                           pic_width_grid,
                                           pic_height_grid, add_up_love, add_up_comment, desc
                                    From share_taobaoke_item
                                    Where category_id =%s
                                    Order by add_up_love desc
                                    Limit %s * (%s-1) ,%s ''',[category_id,page_size,page,page_size])
        return serialize(JSON,item,fields=fields)

    def get_relate_by_user_id(self,user_id,page):
        """
        根据用户ID获取分享的宝贝
        """
        item = self.raw(""" Select item_id,title,price,pic_url_grid,pic_width_grid,
                                    pic_height_grid
                            From share_taobaoke_item
                            Where user_id = %s
                            Order by add_up_love desc
                            Limit 20 * (%s-1), 20
                        """,[user_id,page])
        return item


class Taobaoke_Item(models.Model):
    item_id = models.IntegerField(primary_key=True,unique=True)
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
    #====如下为自定义字段===============================
    user = models.ForeignKey(Account,db_column='user_id')
    #所属分类：衣服；家居；
    category = models.ForeignKey(Category,db_column='category_id')
    #宝贝的简要描述，50个字符内
    desc = models.CharField(max_length=50,null=True)
    share_date = models.DateTimeField(auto_now_add=True,auto_now=True,editable=False)
    add_up_love = models.IntegerField(default=0,editable=False)
    add_up_bookmark = models.IntegerField(default=0,editable=False)
    add_up_comment = models.IntegerField(default=0,editable=False)
    uuid = models.CharField(max_length=32)
        
    #grid page size and pic url
    pic_width_grid = models.IntegerField(null=True)
    pic_height_grid = models.IntegerField(null=True)
    pic_url_grid = models.CharField(max_length=250,null=True)
    #detail page size and pic url
    pic_width_detail = models.IntegerField(null=True)
    pic_height_detail = models.IntegerField(null=True)
    pic_url_detail = models.CharField(max_length=250,null=True)
    #orig pic url
    pic_url_orig = models.CharField(max_length=250,null=True)
    #======/===========================================
    
    # 自定义Manager
    objects = Taobaoke_Item_Manager()

    class Meta():
        ordering = ['-share_date','title']

    def __unicode__(self):
        return self.title



class Tag(models.Model):
    """
    宝贝标签属性
    """
    # 颜色；风格；场合；流行元素；品牌
    TYPE_IN_TAG=(
        ('CO','Color'),
        ('ST','Style'),
        ('OC','Occasion'),
        ('PE','PopularElement'),
        ('BR','Brand'),
    )
    item = models.ForeignKey(Taobaoke_Item,db_column='item_id',unique=False,blank=False)
    tag_id = models.IntegerField()
    type = models.CharField(max_length=2,choices=TYPE_IN_TAG)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)



class Item_Comment(models.Model):
    """
    宝贝评论
    """
    comm_id = models.IntegerField(primary_key=True,unique=True)
    item = models.ForeignKey(Taobaoke_Item,db_column='item_id',unique=False,blank=False)
    user = models.ForeignKey(Account,db_column='user_id',unique=False,blank=False)
    desc = models.CharField(max_length=500,blank=False)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)
    #被赞次数统计
    add_up = models.IntegerField(default=0)
    #回复评论关联ID
    reply_id = models.IntegerField()

    def __unicode__(self):
        return self.desc






































