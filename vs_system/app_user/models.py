from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    middle_name = models.CharField(max_length=64, null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=250, null=True, blank=False)
    contact_number = models.CharField(max_length=11)
    sponsor = models.CharField(max_length=64, null=True, blank=False)
    placement = models.CharField(max_length=64, null=True, blank=False)
    signup_date = models.DateTimeField(null=True)
    signup_package = models.CharField(max_length=24)
    
    def __str__(self):
        return f"{self.username}"
        
            
#     def __str__(self):
#         return self.username
    
#     def get_username(self):
#         return self.username 
    
#     def get_firstname(self):
#         return self.firstname
    
#     def get_lastname(self):
#         return self.lastname
    
#     @property
#     def is_staff(self):
#         return self.is_staff
    
#     @property
#     def is_admin(self):
#         return self.is_admin
    
#     @property
#     def is_active(self):
#         return self.is_active
    
