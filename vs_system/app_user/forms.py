"""
Copyright (c) 2022 - present Michael Denum
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'birth_date',
                  'address', 'contact_number', 'sponsor',
                  'placement', 'signup_date', 'signup_package', 'password1', 'password2')
 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'sponsor': forms.TextInput(attrs={'class': 'form-control'}),
            'placement': forms.TextInput(attrs={'class': 'form-control'}),
            'signup_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'signup_package': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'})
        }
        
        
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username', 'middle_name', 'birth_date',
                  'address', 'contact_number', 'sponsor',
                  'placement', 'signup_date', 'signup_package')


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    
    cap_image = CaptchaField
    captcha = CaptchaField()


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2')
        