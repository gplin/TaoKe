#-*- coding:utf-8 -*-
import datetime
import json
from django.db import models
from django.contrib.auth.models import User
from django.core.serializers import serialize,deserialize
from django.core.serializers.json import DjangoJSONEncoder
from utils.taoke_json import dict2JSON
from account.models import Account

# class CategoryManager(models.Manager):
#     def get_category_tree(self,enable): 
#         li = []
#         cate = list(self.filter(enable=enable).values('category_id','name','parent_id','enable','display_seq','add_up','is_hot','type'))
#         for c in filter(lambda x:x['parent_id']==0,cate):
#             items = filter(lambda x:x['parent_id']==c['category_id'],cate)
#             c['items']=sorted(items,key=lambda x:x['display_seq'])
#             li.append(c)
#         return sorted(li,key=lambda x:x['display_seq'])


# class Category(models.Model):
#     """
#     宝贝类别: 衣服；包包；家居
#     """
#     CLOTHES = "CL" #1
#     SHOES = "SH"   #2 
#     BAGS = "BA"  #3包包
#     ACCESSORIES = "AC" #4配饰
#     HOME = "HO" #5家居
#     CREATIVE = "CR" #6创意
#     COSMETICS = "CO" #7美容
#     TYPE_CHOICES = (
#         (CLOTHES,'Clothes'),
#         (SHOES,'Shoes'),
#         (BAGS,'Bags'),
#         (ACCESSORIES,'Accessories'),
#         (HOME,'Home'),
#         (CREATIVE,'Creative'),
#         (COSMETICS,'Cosmetics'),
#     )
#     category_id = models.AutoField(primary_key=True,null=False,unique=True)
#     name = models.CharField(max_length=20,blank=False,unique=True,help_text='分类名称')
#     parent_id = models.IntegerField(default=0)
#     enable = models.BooleanField(default=True)
#     init_date = models.DateTimeField(auto_now_add=True,editable=False)
#     display_seq =models.IntegerField(default=0)
#     add_up = models.IntegerField(default=0)
#     is_hot= models.BooleanField(default=False)
#     type = models.CharField(max_length=2,choices=TYPE_CHOICES)

#     objects = CategoryManager()

#     class Meta():
#         ordering = ['display_seq','enable','init_date','name']

#     def __unicode__(self):
#         return u'%s' % unicode(self.name)

#     def __str__(self):
#         return self.__unicode__()

class Item_Cats(models.Model):
    """
    淘宝类目
    """
    CLOTHES = "CL" #1 衣服
    SHOES = "SH"   #2 　鞋子
    BAGS = "BA"  #3包包
    ACCESSORIES = "AC" #4配饰
    HOME = "HO" #5家居
    CREATIVE = "CR" #6创意
    COSMETICS = "CO" #7美容
    TYPE_CHOICES = (
        (CLOTHES,'Clothes'),
        (SHOES,'Shoes'),
        (BAGS,'Bags'),
        (ACCESSORIES,'Accessories'),
        (HOME,'Home'),
        (CREATIVE,'Creative'),
        (COSMETICS,'Cosmetics'),
    )

    cid = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=50,blank=False,help_text='分类名称')
    parent_cid = models.IntegerField(default=0)
    is_parent = models.BooleanField(default=True)
    status = models.CharField(max_length=10,null=True)
    sort_order = models.IntegerField(null=True)
    
    #  自定义增加
    enable = models.BooleanField(default=False)
    display_seq =models.IntegerField(default=0,null=True)
    add_up = models.IntegerField(default=0,null=True)
    is_hot= models.NullBooleanField(default=False,null=True)
    type = models.CharField(max_length=2,choices=TYPE_CHOICES,null=True)
    nickname = models.CharField(max_length=10,null=True)
    is_menu = models.NullBooleanField(default=False,null=True)



    class Meta():
        ordering = ['display_seq','enable','name']

    def __unicode__(self):
        return u'%s' % unicode(self.name)

    def __str__(self):
        return self.__unicode__()

class Item_Style(models.Model):
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


class Item_Popular_Element(models.Model):
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


class Item_Brand(models.Model):
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


class Item_Color(models.Model):
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
    

class Item_Occasion(models.Model):
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


class Item_Manager(models.Manager):
    """
    """
    def get_main_sql(self):
        return '''
                Select user.id as user_id, user.username, acc.icon,
                       cate.[type], cate.cid,cate.name as cats,
                       item.item_id,item.title,item.price, item.pic_url_grid,
                       item.pic_width_grid,item.pic_height_grid,
                       add_up_love, add_up_comment, 
                       case When item.comment is not null Then item.comment else '' end as desc,
                       case When love.account_id is not null Then 'Y' else 'N' end as loved,
                       case When item.account_id =love.account_id Then 'Y' else 'N' End as self
                From share_item item
                inner join
                     share_item_cats cate on item.cid = cate.cid
                inner join                             
                     auth_user user on user.id = item.account_id
                inner join                            
                     account_account acc on acc.user_id = user.id     
                Left Join                
                     share_item_love love on item.item_id =love.item_id and love.account_id=%s  
                where active=1  
                '''

    def get_order_sql(self):
        return '''
               Order by add_up_love desc, add_up_bookmark desc, add_up_comment desc  

               '''

    def get_limit_sql(self,page,page_size=20):
        if page:
            # page = page if page else 1
            page_size = page_size if page_size else 20
            return ' Limit %s * (%s-1) ,%s ' % (page_size,page,page_size)
        else:
            return ''

    def get_item_default(self,page,page_size=20,user_id=None):
        """
        """
        sql = '%s%s%s' % (self.get_main_sql(),self.get_order_sql(),self.get_limit_sql(page,page_size))
        item =self.raw(sql,[user_id])
        return self.serialize_to_json(item)

    def get_item_by_user_id(self,user_id,page,page_size=20):
        """
        根据用户ID获取分享的宝贝
        """
        # sql = '%s%s%s%s' % (self.get_main_sql(),'Where acc.user_id = %s',
        #                     self.get_order_sql(),self.get_limit_sql(page,page_size)
        #                    )
        # item = self.raw(sql,[user_id])
        # return self.serialize_to_json(item)
        if user_id is None: 
            raise ValueError(u'user_id must be set')
        if page is None:
            raise ValueError(u'page must be set')
        return self.get_item_default(page,page_size,user_id)

    def get_item_by_category(self,user_id=None,type=None,category_id=None,page=None,page_size=20):
        """
        根据分类ID,页码,获取分享的宝贝
        """
        type = type.upper() if type else None
        sql = '%s%s%s%s' % (self.get_main_sql(),
                            '''   and (cate.cid = %s or %s is null) 
                                  and (cate.[type]=%s or %s is null)
                            ''',
                            self.get_order_sql(),self.get_limit_sql(page,page_size)
                           )
        item = self.raw(sql,[user_id,category_id,category_id,type,type])
        return self.serialize_to_json(item)

    def serialize_to_json(self,data):
        """
        将models.Mode或RawQuerySet或QuerySet序列化为JSON格式,
        包含Item外键关联的字段:
            user:     user_id, username,icon;
            category: category_id,category_name,type
        """
        data = data if not isinstance(data,models.Model) else [data]
        result = []
        for item in data:
            tmp = item.__dict__
            result.append(tmp)
        return dict2JSON(result)

    def save_item_from_detail_get(self,account_id,data,pic):
        u"""
        保存top.api: taobaoke.items.detail.get 获取的数据,返回 Item
        fields: 
                num_iid, title, price, pic_url, click_url, desc, cid, location, one_station
                detail_url,shop_click_url, seller_credit_score, 
        """
        if account_id is None:
            valueError("account_id must be set")
        if data is None:
            valueError("data must be set")
        # if isinstance(data,dict):
        #     valueError("parameter 'data' must be dict type")
        account = Account.objects.get(user_id=account_id)
        item_cats = Item_Cats.objects.get(cid=data["item"]["cid"])
        item = self.create( account=account,
                            item_cats=item_cats,
                            num_iid=data["item"]["num_iid"],
                            title=data["item"]["title"],
                            price=data["item"]["price"],
                            pic_url=data["item"]["pic_url"],
                            # desc=data["item"]["desc"],
                            # location=data["item"]["location"],
                            one_station=data["item"]["one_station"],
                            detail_url=data["item"]["detail_url"],
                            click_url=data["click_url"],
                            shop_click_url=data["shop_click_url"],
                            seller_credit_score=data["seller_credit_score"],
                            pic_url_orig=pic["pic_url_orig"],
                            pic_width_grid=pic["pic_width_grid"],
                            pic_height_grid=pic["pic_height_grid"],
                            pic_url_grid=pic["pic_url_grid"],
                            pic_width_detail=pic["pic_width_detail"],
                            pic_height_detail=pic["pic_height_detail"],
                            pic_url_detail=pic["pic_url_detail"],
                            uuid=pic["uuid"],
                            active=False
                           )
        # item.save()
        return item

    def update_comment_active(self,uuid,comment):
        u"active, comment"
        item=self.get(uuid=uuid)
        item.active=True
        item.comment=comment
        item.save()
        return item


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True,unique=True)
    # item common fileds
    num_iid = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    nick = models.CharField(max_length=50)
    pic_url = models.CharField(max_length=500)          #商品主图片地址
    location = models.CharField(max_length=100)         #商品所在地
    price = models.DecimalField(max_digits=20,decimal_places=6)
    click_url = models.CharField(max_length=500)
    shop_click_url = models.CharField(max_length=500)
    seller_credit_score = models.DecimalField(max_digits=10,decimal_places=0)

    # TaobaokeItem(taobaoke.items.get)
    seller_id = models.CharField(max_length=50,null=True)
    taobaoke_cat_click_url = models.CharField(max_length=500,null=True)
    keyword_click_url = models.CharField(max_length=500,null=True)
    coupon_rate = models.CharField(max_length=50,null=True)
    coupon_price = models.DecimalField(max_digits=20,decimal_places=6,null=True)
    coupon_start_time = models.CharField(max_length=20,null=True)
    coupon_end_time = models.CharField(max_length=20,null=True)
    commission_rate = models.CharField(max_length=20)
    commission = models.DecimalField(max_digits=20,decimal_places=6,null=True)
    commission_num = models.CharField(max_length=20,null=True)
    commission_volume = models.DecimalField(max_digits=20,decimal_places=0,null=True)
    shop_type = models.CharField(max_length=5,null=True)
    volume = models.DecimalField(max_digits=30,decimal_places=2,null=True)
    
    # Item(taobaoke.items.detail.get)
    detail_url = models.CharField(max_length=500,null=True)      #商品URL
    type = models.CharField(max_length=10,null=True)             #商品类型
    desc = models.CharField(max_length=25000,null=True)
    # skus
    props_name = models.CharField(max_length=500,null=True)      #商品属性名称
    created = models.DateTimeField(null=True)                   #Item 的发布时间
    promoted_service = models.CharField(max_length=10,null=True) #消保类型: 假一赔三 ...
    is_lightning_consignment = models.NullBooleanField(null=True)   #是否24小时闪电发货
    is_fenxiao = models.IntegerField(null=True)                 #是否分销商品: 非分销商品: 0; 代销: 1;经销:2;
    auction_point = models.DecimalField(max_digits=5,decimal_places=2,null=True) #天猫订单抽用比例,为5的倍数,最低0.5%,与淘客用金没有关系
    property_alias = models.CharField(max_length=100,null=True)  #属性值别名
    # template_id 页面模板id
    # after_sale_id 售后服务ID 
    is_xinpin = models.NullBooleanField(null=True)                  #标示商品是否为新品
    # sub_stock
    sell_point = models.CharField(max_length=15,null=True)      #商品卖点信息,天猫商品使用字符
    outer_id = models.CharField(max_length=50,null=True)        #商家外部编码,需要授权才能获取
    # cid = models.IntegerField(null=True)                       #商品所属的叶子类目ID
    props = models.CharField(max_length=500,null=True)          #商品属性. 
    product_id = models.IntegerField(null=True)                #宝贝所属产品ID,
    # item_imgs 商品图片列表
    # prop_imgs 商品属性图片列表
    score = models.IntegerField(null=True)#商品卖家的信用等级数  
    one_station = models.NullBooleanField(null=True)               #是否淘1站商品
    # second_kill 


    #====如下为自定义字段===============================
    account = models.ForeignKey(Account,db_column='account_id')
    #所属分类：衣服；家居；
    item_cats = models.ForeignKey(Item_Cats,db_column='cid')
    #宝贝的简要描述，50个字符内
    comment = models.CharField(max_length=50,null=True)
    share_date = models.DateTimeField(auto_now_add=True,auto_now=True,editable=False)
    add_up_love = models.IntegerField(default=0,editable=False,null=True)
    add_up_bookmark = models.IntegerField(default=0,editable=False,null=True)
    add_up_comment = models.IntegerField(default=0,editable=False,null=True)
    uuid = models.CharField(max_length=32,null=True)
        
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
    
    # temp
    active = models.BooleanField(default=False)

    # 自定义Manager
    objects = Item_Manager()

    class Meta():
        ordering = ['-share_date','title']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def serializers_to_json(self):
        u"""serializer fields: 
            item_id,title,pic_url_grid,price,account_id
        """
        data=dict(item_id=self.item_id,
                  title=self.title,
                  price=self.price,
                  account_id=self.account_id,
                  pic_width_grid=self.pic_width_grid,
                  pic_height_grid=self.pic_height_grid,
                  pic_url_grid=self.pic_url_grid,
                  uuid=self.uuid)
        return dict2JSON(data)


class Item_Tag(models.Model):
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
    item = models.ForeignKey(Item,db_column='item_id',unique=False,blank=False)
    tag_id = models.IntegerField()
    type = models.CharField(max_length=2,choices=TYPE_IN_TAG)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)



class Item_Comment(models.Model):
    """
    宝贝评论
    """
    comm_id = models.IntegerField(primary_key=True,unique=True)
    item = models.ForeignKey(Item,db_column='item_id',unique=False,blank=False)
    user = models.ForeignKey(Account,db_column='user_id',unique=False,blank=False)
    desc = models.CharField(max_length=500,blank=False)
    init_date = models.DateTimeField(auto_now_add=True,editable=False)
    #被赞次数统计
    add_up = models.IntegerField(default=0)
    #回复评论关联ID
    reply_id = models.IntegerField(unique=False,null=True)

    def __unicode__(self):
        return self.desc


class Item_Love_Manager(models.Manager):

    def set_item_love(self,item_id,account_id):
        item = Item.objects.get(item_id=item_id)
        account = Account.objects.get(user_id=account_id)
        love, created = self.get_or_create(item=item,account=account)
        if not created:
            love.delete()
        return dict(instance=love,created=created)


class Item_Love(models.Model):
    """用户喜爱的商品"""
    item = models.ForeignKey(Item,db_column='item_id',blank=False,null=False)
    account = models.ForeignKey(Account,db_column="account_id",blank=False,null=False)
    datetime = models.DateTimeField(auto_now_add=True,editable=False)

    objects = Item_Love_Manager()

    class Meta():
        unique_together=(("item","account"),)
        ordering = ['account','item','-datetime']

    def __unicode__(self):
        return  u'%s : %s love %s' % (self.datetime,self.account.user.username,self.item.title)
        


































