from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Count
from .forms import *
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
    line_pending = orders.filter(status='To Be Planned').count()
    line_planned = orders.filter(status='Planned').count()
    total_customers = customers.count()
    context = {'orders':orders,'customers':customers,'cust_orders':cust_orders,
    'total_orders':total_orders,'line_pending':line_pending,'line_planned':line_planned}
    return render(request, 'custmanager/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'custmanager/products.html',{'products':products})

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    po_count = Order.objects.values('ponumber').order_by().annotate(Count('ponumber',distinct=True))
    context = {'customer':customer,'orders':orders,'po_count':po_count}
    return render(request, 'custmanager/customer.html',context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'custmanager/order_form.html',context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        #print(request.POST)
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'custmanager/order_form.html',context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request,'custmanager/delete.html',context)
