"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include('app01.urls', namespace='app01')),
    path('users/', include('users.urls', namespace='users')),
    # 法律文书生成app
    path('make_document/', include('make_document.urls', namespace='make_document')),
    # 配置favicon.ico文件
    path('favicon.ico/', RedirectView.as_view(url=r'static/favicon.ico')),
]
