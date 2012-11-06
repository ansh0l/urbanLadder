from django.template import RequestContext, loader, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from product.models import *

def search_suggestions_for_products(search_string):
    suggestions = []
    #query = 'select * from product_product where name like "%s%s%s"' %('%', search_string, '%')
    #suggestions = Product.objects.raw(query)
    suggestions = Product.objects.filter(name__contains = search_string)
    return suggestions

def increment_current_page(request):
    try:
        curr = int(request.session['page_number'])
        curr += 1
        request.session['page_number'] = curr
        #request.session.save()
    except:
        pass

def decrement_current_page(request):
    errors = []
    try:
        curr = int(request.session['page_number'])
        if curr >1:
            curr -= 1
            request.session['page_number'] = curr
            #request.session.save()
        else:
            errors.append("Cannot go to previous page from here")
    except:
        pass
    return errors

def update_page_and_record_per_page_settings(request):
    errors = []
    try:
        page_number = int(request.POST.get('page_number'))
        records_per_page = int(request.POST.get('records_per_page'))
        if records_per_page or page_number:
            if page_number and page_number<1:
                errors.append("invalid page number passed")
            else:
                request.session['page_number'] = page_number
                #request.session.save()
            if records_per_page and records_per_page<2:
                errors.append("invalid records per page value passed")
            else:
                request.session['records_per_page'] = records_per_page
                #request.session.save()
        else:
            errors.append("No settings to update")
    except:
        errors.append("error occured while updating settings")
    return errors
        
def set_search_string(request):
    request.session['search_string'] = request.POST.get('search_string')
    #request.session.save()

def init_request(request):
    request.session['page_number'] = 1
    request.session['search_string'] = '' 
    request.session['records_per_page'] = 50
    #request.session.save()
