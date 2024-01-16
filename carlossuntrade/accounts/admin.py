from django.contrib import admin

# Register your models here.
from .models import *  # that point can be replaced by 'accounts' and * represents all models
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)