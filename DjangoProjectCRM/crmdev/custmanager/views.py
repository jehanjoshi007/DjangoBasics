from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Count
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
    total_orders = Order.objects.values('ponumber').order_by().annotate(Count('ponumber',distinct=True))
#    order_sum = total_orders.aggregate(sum())
#    count_orders = total_orders.count()
    total_customers = customers.count()
    context = {'orders':orders,'customers':customers,'cust_orders':cust_orders,
    'total_orders':total_orders}
    return render(request, 'custmanager/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'custmanager/products.html',{'products':products})

def customer(request):
    return render(request, 'custmanager/customer.html')
