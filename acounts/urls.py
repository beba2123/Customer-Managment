from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('update_customer/<str:pk>', views.update_order, name='update_customer'),
    path('create_order/<str:pk>', views.create_order, name="create_order"),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
]


