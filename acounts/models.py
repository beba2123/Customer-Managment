from django.db import models
import uuid
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) #establish the connection between the customer and login user.
    name = models.CharField(max_length=200, blank=True, null=True)
    Email = models.EmailField(max_length=200)
    profile_pic = models.ImageField(default="profile-icon-png-898.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 

class Tags(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name;

class Product(models.Model):
    CATAGORY = (
        ('Indoor', 'indoor'),
        ('Out-Door', 'Out-Door'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.FloatField(default=0, blank=False, null=False)
    category = models.CharField(max_length=200, blank=True, null=False, choices=CATAGORY)
    description = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(default = 0, blank=False, null = False)
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tags)
    
    def __str__(self):
        return self.name;
class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'out for delivery'),
            ('Delivered', 'Delivered'),
            )
    customer  = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True, choices=STATUS)
    note = models.CharField(max_length=500,null=True)
    
    def __str__(self):
        return self.product.name;