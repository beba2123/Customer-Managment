from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = PhoneNumberField()
    Email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# class Product(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                          primary_key=True, editable=False)
#     name = models.CharField(max_length=200, blank=False, null=False)
#     price = models.IntegerField(default=0, blank=False, null=False)
#     quantity = models.IntegerField(default = 0, blank=False, null = False)
#     date_created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name;


