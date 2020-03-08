from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

#Always remember this folder structure to render templates
#--appname
#----templates
#------appname
#--------template.html

def Home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    cust_orders = Order.objects.select_related('customer','product').order_by('ponumber','linenumber').all()
    context = {'orders':orders,'customers':customers,'cust_orders':cust_orders}
    return render(request, 'custmanager/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'custmanager/products.html',{'products':products})

def customer(request):
    return render(request, 'custmanager/customer.html')
