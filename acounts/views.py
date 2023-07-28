from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    totalOrders = orders.count()
    order_delieverd = orders.filter(status = 'Delivered').count()
    order_pending = orders.filter(status = 'Pending')
    context = {'orders': orders, 'customers': customers,'order-delivered': order_delieverd, 'order-pending': order_pending, ' totalOrders': totalOrders}
    return render(request, 'acounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return  render(request,'acounts/products.html', {'products': products})

def customer(request):
    return render(request, 'acounts/customer.html')
