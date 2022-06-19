from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.Register(Product)
admin.site.Register(Category)