from django.template import RequestContext, loader, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from order.models import *

def order_landing(request):
    page_number=request.GET.get('page', 1)
    item_per_page = request.session.get('item_per_page', 50)
    order_start = (page_number-1)*(item_per_page)
    order_end = order_start + item_per_page 
    orders = Order.objects.all()[order_start:order_end]
    context_dict = {
        'orders': orders,
    }
    return render_to_response('order.html', context_dict, context_instance = RequestContext(request))

def set_item_per_page(request):
    if request.method == 'POST':
        item_per_page = request.POST.get('item_per_page', '50')
        request.session['item_per_page'] = 50
        request.session.save()
        order_landing(request)
    raise Http404
