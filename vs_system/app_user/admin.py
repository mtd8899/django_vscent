from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser

# Register your models here.
class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'first_name', 'middle_name', 'last_name', 'email', 'address', 'contact_number', 'sponsor', 'placement', 'signup_date', 'signup_package']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('middle_name', 'birth_date', 'address', 'contact_number')}),)
    # Make fields editable.
    
admin.site.register(MyUser,MyUserAdmin)