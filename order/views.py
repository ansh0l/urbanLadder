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
            init_request(request)
            set_search_string(request)
    else:
        init_request(request)
    return errors

def order_landing(request):
    orders, errors, orders_set, order = [], [], [], None
    errors = order_handle_request(request)

    page_number = request.session.get('page_number')
    records_per_page = request.session.get('records_per_page')
    search_string = request.session.get('search_string')

    total_items = Order.objects.count()
    order_start = (page_number-1)*(records_per_page)
    order_end = order_start + records_per_page 

    try:
        order = int(request.POST.get('order'))
        if order and order<1:
            errors.append("Invalid order value")
    except:
        pass

    if search_string:
        if not order:
            ois = OrderItem.objects.filter(product__name__contains = search_string)
            for oi in ois:
                if oi.order not in orders_set:
                    orders_set.append(oi.order)
            total_items = len(orders_set)
            if order_start < total_items:
                orders = orders_set[order_start:order_end]
            else:
                errors.appends("No orders for given range")
        else:
            ois = OrderItem.objects.filter(product__name__contains = search_string, order=order)
            if ois:
                orders.append(ois[0].order)
                total_items=len(orders)
            else:
                errors.append("No orders for given query")
    elif order:
        ois = OrderItem.objects.filter( order=order)
        if ois:
            orders.append(ois[0].order)
            total_items=len(orders)
        else:
            errors.append("No orders for given query")
    else:
        try:
            orders = Order.objects.all()[order_start:order_end]
        except:
            errors.append("No orders found")
    
    details = {
        'total_items': total_items,
        'page_number': page_number,
        'records_per_page': records_per_page,
        'order':order,
        'search_string': search_string}

    context_dict = {
        'errors' : errors,
        'details' : details, 
        'orders' : orders,
    }
    context_instance = RequestContext(request)

    return render_to_response('order.html', context_dict, context_instance )
