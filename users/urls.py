"""为应用程序users 定义URL模式**"""
from django.conf.urls import url
from django.urls import path, include
# from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    # 'login'后面必须得有一个'/'符号
    url('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销
    url('logout/', views.logout_view, name='logout'),
    # 注册页面
    url('register/', views.register, name='register'),
]
