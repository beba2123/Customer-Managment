from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('update_customer/<str:pk>', views.update_order, name='update_customer'),
    path('create_order/<str:pk>', views.create_order, name="create_order"),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
    path('login/', views.loginPage, name='login'),
     path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('user_profile', views.user_page, name='user_profile'),
]