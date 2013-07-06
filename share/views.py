#-*- coding:utf-8 -*-
from django.utils import simplejson
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render,get_object_or_404
from django.core.urlresolvers import reverse
from django.core.serializers import serialize,deserialize
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext

from polls.models import Poll, Choice
from share.models import Taobaoke_Item

def index(request):
    items = Taobaoke_Item.objects.all()
    return render_to_response('share/index.html',{'items':items},
                              context_instance=RequestContext(request))

def JSON(request,page):
    page = page if page else 1
    if request.is_ajax():
        item = Taobaoke_Item.objects.raw('''Select rec_num,
                                           nick,
                                           title,
                                           price,
                                           pic_local_url_second,
                                           pic_width_second,
                                           pic_height_second
                                    From share_taobaoke_item
                                    Order by rec_num asc
                                    Limit 20 * (%s-1) ,20 ''',[page])
        return HttpResponse(serialize('json',item,fields=('rec_num','nick','price','click_url','title',
                                                      'pic_local_url_second',
                                                      'pic_width_second',
                                                      'pic_height_second')
                                      ),
                            mimetype='application/json')
    
# @csrf_exempt
def Demo1(request):
    if request.is_ajax():
        item = Taobaoke_Item.objects.all()
    return HttpResponse(serialize('json',item,fields=('rec_num','nick','click_url','title',
                                                      'pic_local_url_second',
                                                      'pic_width_second',
                                                      'pic_height_second')
                                    ),
                        mimetype='application/json')
