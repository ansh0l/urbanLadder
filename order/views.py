from django.template import RequestContext, loader, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from order.models import *
#from utils.views import search_suggestions, increment_current_page, decrement_current_page 
from utils.views import *

def order_handle_request(request):
    errors = []
    if request.method=='POST': 
        if request.POST.get('submit')=='reset':
            init_request(request)
        elif request.POST.get('submit') == 'update_settings':
            errors = update_page_and_record_per_page_settings(request)
        elif request.POST.get('submit') == 'next':
            increment_current_page(request)
        elif request.POST.get('submit') == 'prev':
            errors = decrement_current_page(request)
        elif request.POST.get('submit') == 'search':
            set_search_string(request)
    else:
        init_request(request)
    return errors

def order_landing(request):
    orders, errors = [], []
    errors = order_handle_request(request)
    page_number = request.session.get('page_number')
    records_per_page = request.session.get('records_per_page')
    search_string = request.session.get('search_string')
    details = {
        'page_number': page_number,
        'records_per_page': records_per_page,
        'search_string': search_string}

    order_start = (page_number-1)*(records_per_page)
    order_end = order_start + records_per_page 
    if search_string:
        product_suggestions = search_suggestions_for_products(search_string)
        ois = OrderItem.objects.filter(product__in = product_suggestions)
        order = []
        for oi in ois:
            if oi.order not in order:
                order.append(oi.order)
        if order_start < len(order):
            orders = order[order_start:order_end]
    else:
        try:
            orders = Order.objects.all()[order_start:order_end]
        except:
            errors.append("No orders found")

    if not orders:
        errors.append("No orders found")

    context_dict = {
        'errors' : errors,
        'details' : details, 
        'orders' : orders,
    }
    context_instance = RequestContext(request)

    return render_to_response('order.html', context_dict, context_instance )
