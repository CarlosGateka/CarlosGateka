from django.contrib import admin
from django.urls import path,include,re_path 
from . import views
from django.urls import re_path as url

context={admin,include,re_path,url}

urlpatterns = [
    path('', views.home,name="home"),
    path('update_order/<str_pk>/', views.createOrder, name="update_order"),
    path('products', views.products,name='products'),
    path('customer/<str:pk_test>/', views.customer,name="customer"),
    path('create_order/', views.createOrder,name="create_order"),
    
   
   
    ]