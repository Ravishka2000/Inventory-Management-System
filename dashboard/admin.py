from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


# change header of the admin Dashboard
admin.site.site_header = 'No Way Inventory Dashboard'


# change the view of the admin dashboard tables
class ProductAdmin(admin.ModelAdmin):
    # define columns to display in tabular format
    list_display = ('name', 'category', 'quantity')
    # generate a filter section
    list_filter = ['category']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)

