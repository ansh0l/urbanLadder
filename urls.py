from django.conf.urls import patterns, include, url
#from django.conf import settings
from django.contrib import admin
from order.views import order_landing, set_item_per_page 
from utils.views import search_suggestions

admin.autodiscover()

#admin panel
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += patterns('utils.views',
#    url(r'^search_suggestions/', search_suggestions),
#)

#order display page
urlpatterns += patterns('order.views',
    url(r'', order_landing),
)
