"""
Copyright (c) 2019 - present Michael Denum
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from app_user import views as app_user_views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout")
    path('logout/', app_user_views.logout_user, name='logout'),
    path('register', app_user_views.UserRegisterView, name='member-signup'),
]
