from django.urls import path
from . import views

#Here the '' indicates base url redirects to Home

urlpatterns = [
    path('', views.Home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/<str:pk>',views.createOrder, name="create_order"),
    path('update_order/<str:pk>',views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>',views.deleteOrder, name="delete_order"),
    path('register/', views.register, name="register"),
    path('loginpage/', views.loginpage, name="login"),
    path('logoutUser/', views.logoutUser, name="logout")

]
