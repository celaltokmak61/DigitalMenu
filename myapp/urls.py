from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('products/', views.all_products, name='all_products'),
    path('category/<slug:slug>/',
         views.category_detail,
         name='category_detail'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/',
         views.category_products,
         name='category_products'),
]
