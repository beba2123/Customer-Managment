# from django.db import models
# import uuid

# # Create your models here.
# class product_type(models.Model):
#  id = models.UUIDField(default=uuid.uuid4, unique=True,
#                          primary_key=True, editable=False)
#  type = models.CharField(max_length=200, blank=False, null=False)

# class Product(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                          primary_key=True, editable=False)
#     name = models.CharField(max_length=200, blank=False, null=False)
#     price = models.IntegerField(default=0, blank=False, null=False)
#     quantity = models.IntegerField(default = 0, blank=False, null = False)
#     date_created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name;


