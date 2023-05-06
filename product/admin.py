from django.contrib import admin
from .models import Category, Tag, Manufacturer, Product

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Manufacturer)
admin.site.register(Product)
