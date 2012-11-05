from django.template import RequestContext, loader, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from product.models import *

def search_suggestions(request):
    suggestions = []
    if request.method == 'POST':
        #search_string = request.POST.get('search_string', 'tab')
        #query = 'select * from product_product where name like "%s%s%s"' %('%', search_string, '%')
        #suggestions = Product.objects.raw(query)
        search_string = request.POST.get('search_string', 'tab')
        suggestions = Product.objects.filter(name__contains = search_string)
    return suggestions
