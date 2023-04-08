from django.contrib import admin
from .models import Category, Product, SiteSettings

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SiteSettings)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_tag')


# Register your models here.
