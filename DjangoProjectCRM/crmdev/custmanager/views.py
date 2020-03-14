from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from django.db.models import Count
from .forms import *
from .filters import *
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

#Always remember this folder structure to render templates
#--appname
#----templates
#------appname
#--------template.html

def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for'  +  user)
                return redirect('login')
        context={'form':form}
        return render(request,'custmanager/register.html',context)

def loginpage(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:

        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')

            else:
                messages.info(request, 'Username or Password is incorrect')
                return render(request,'custmanager/login.html')

        context = {}
        return render(request,'custmanager/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'custmanager/products.html',{'products':products})

@login_required(login_url='login')
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    po_count = Order.objects.values('ponumber').order_by().annotate(Count('ponumber',distinct=True))
    my_filter = OrderFilter(request.GET,queryset=orders)
    orders = my_filter.qs
    context = {'customer':customer,'orders':orders,'po_count':po_count,'my_filter':my_filter}
    return render(request, 'custmanager/customer.html',context)

@login_required(login_url='login')
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('ponumber','customer','linenumber','product','price','QuantityY2','QuantityRolls','status'),extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print(request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        #print(formset)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'custmanager/order_form.html',context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request,'custmanager/delete.html',context)

# def listing(request):
#     order_list = Order.objects.select_related('customer','product').order_by('ponumber','linenumber').all()
#     paginator = Paginator(order_list,2)
#     page_request_var = "page"
#     page = request.GET.get(page_request_var)
#     try:
#         queryset = paginator.page(page)
#     except PageNotAnInteger:
#         queryset = paginator.page(1)
#     except EmptyPage:
#         queryset = paginator.page(paginator.num_pages)
#
#     context = {
#         "object_list":queryset,
#         "title":"list",
#         "page_request_var":page_request_var,
#         "order_list":order_list}
#     return render(request, 'custmanager/dashboard.html', context)
