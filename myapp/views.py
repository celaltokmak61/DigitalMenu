from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SiteSettings
from constance import config

def index(request):
    categories = Category.objects.all()
    return render(request, 'myapp/index.html', {'categories': categories})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'myapp/products.html', {'products': products})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(active=True)
    return render(request, 'myapp/category_detail.html', {'category': category, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'myapp/product_detail.html', {'product': product})

def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.filter(active=True)
    return render(request, 'myapp/category_detail.html', {'category': category, 'products': products})

def about(request):
    return render(request, 'myapp/about.html')

def my_view(request):    
    context = {'SITE_name': config.SITE}
    return render(request, 'index.html', context)

  





 