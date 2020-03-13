from django.urls import path
from . import views

#Here the '' indicates base url redirects to Home

urlpatterns = [
    path('', views.Home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
]
