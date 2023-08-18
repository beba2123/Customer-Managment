from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters  import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data['username']
            messages.success(request, user + ' created account successfully ')
            return  redirect('login')

    context = {'form': form}
    return render(request, 'acounts/register.html', context)

def loginPage(request):
    context={}
    return render(request, 'acounts/login.html', context)

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    order_delieverd = orders.filter(status = 'Delivered').count()
    order_pending = orders.filter(status = 'Pending').count()
    context = {'orders': orders, 'customers': customers,'order_delivered': order_delieverd, 'order_pending': order_pending, 'total_orders': total_orders}
    return render(request, 'acounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return  render(request,'acounts/products.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs

    context = {'customer': customer, 'orders': orders, 'orders_count':orders_count, 'myfilter':myfilter}
    return render(request, 'acounts/customer.html', context)

def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("product", "status"), extra=5)
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer':customer}) before we create inline form sets
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        # print('printing post', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        

    context={'formset':formset}
    return render(request, 'acounts/create_form.html', context)

def update_order(request, pk):
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) #the instance of the order table before we update it the previous information that we submited it.
    
    if request.method == 'POST':
     form = OrderForm(request.POST, instance=order)
     if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'acounts/create_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST': #if we say confirm
        order.delete() #the order is going to be deleted 
        return redirect('/') # then we will be redirect to the home page 
    context={'item':order}

    return render(request, 'acounts/delete_order.html', context)