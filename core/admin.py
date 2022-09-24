from django.contrib import admin

# Models
from .models import Factory, Product

# Register your models here.
admin.site.register(Factory)
admin.site.register(Product)
