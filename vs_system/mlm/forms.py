from datetime import date
from email.policy import default
from enum import auto
from sqlite3 import Date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm): 
    def make_fullname(self):
         fullname = f"{self.first_name} {self.middle_name} {self.last_name}"
         return str(fullname)
    
    first_name = forms.CharField(max_length=64)
    middle_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    address = forms.CharField(max_length=250)
    birth_date = forms.DateField(help_text="Format: YYYY-MM-DD")
    address = forms.CharField(max_length=250)
    contact_number = forms.CharField(max_length=11)
    sponsor = forms.CharField(max_length=64)
    placement = forms.ChoiceField(choices=[("FL", "Far Left"),("FR", "Far Right")])
    # signup_date = forms.DateField()
    signup_package = forms.ChoiceField(choices=[("P1", "Product 1")])
   
    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'username', 'email',
                  'password1', 'password2', 'birth_date', 'address', 'contact_number',
                  'sponsor', 'signup_package', 'placement')