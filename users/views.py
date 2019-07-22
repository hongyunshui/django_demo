# 在这里创建自定义视图.
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from django.urls import reverse


def logout_view(request):
    """"注销用户**"""
    logout(request)
    return HttpResponseRedirect(reverse('app01:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 如果使请求则返回一个新的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        # 如果填写的表单有效则进行如下操作
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('app01:index'))
    context = {'form': form}
    # 跳转到注册页面
    return render(request, 'users/register.html', context)
