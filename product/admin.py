from django.contrib import admin
from .models import Product, Brand, Category, ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImage)

