from django.contrib import admin
from .models import Orders
from .models import Products
from .models import Services


admin.site.register(Orders)
admin.site.register(Products)
admin.site.register(Services)
