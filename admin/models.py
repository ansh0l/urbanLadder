from django.contrib import admin
from django import forms
from django.db.models import *
from customer.models import *
from product.models import *
from order.models import *

class CityStateAdmin(admin.ModelAdmin):
    list_display = ('city','state')
    search_fields = ('city','state')
admin.site.register(CityState, CityStateAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','address', 'citystate', 'pincode', 'mobile')
    search_fields = ['name', 'email','address', 'citystate', 'pincode', 'mobile']
admin.site.register(Customer, CustomerAdmin)

#class FeatureAdmin(admin.ModelAdmin):
#    list_display = ('name','description')
#    search_fields = ['name','description']
#admin.site.register(Feature, FeatureAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('description','name', 'slug', 'price')
    search_fields = ['description','name', 'slug', 'price']
admin.site.register(Product, ProductAdmin)

#class ProductFeatureMapAdmin(admin.ModelAdmin):
#    list_display = ('feature', 'product')
#    search_fields = ['feature', 'product']
#admin.site.register(ProductFeatureMap, ProductFeatureMapAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','date', 'amount', 'payment_method', 'payment_realised')
    search_fields = ['customer','date', 'amount', 'payment_method', 'payment_realised']
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product', 'order')
    search_fields = ('quantity', 'product', 'order')
admin.site.register(OrderItem, OrderItemAdmin)
