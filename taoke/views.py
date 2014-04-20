from django.shortcuts import render_to_response, render,get_object_or_404
from django.template import RequestContext
from share.views import share



def home(request):
    """
    """
    return share(request,'df')
    # cid=request.GET.get("cid")
    # return render_to_response('share/main.html',{"cats":'df',"cid":cid},context_instance=RequestContext(request))