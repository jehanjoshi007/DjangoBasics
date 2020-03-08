from django.urls import path
from . import views

#Here the '' indicates base url redirects to Home

urlpatterns = [
    path('', views.Home),
    path('products/', views.products),
    path('customer/', views.customer),
]
