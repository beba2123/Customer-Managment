from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

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
    context = {'customer': customer, 'orders': orders, 'orders_count':orders_count}
    return render(request, 'acounts/customer.html', context)
