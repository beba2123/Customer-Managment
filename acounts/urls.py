from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views
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
    path('acounts/', views.accountSettings, name="accounts"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset-password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_successfully', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
