from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<category_id>', views.product_list, name='product-list'),
    path('product-detail/<product_id>', views.product_detail, name='product-detail'),
    path('register/', views.register, name="register"),
]
