from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import NaturalPerson, Enterprise
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NaturalPersonForm, EnterpriseForm
from django.urls import reverse
# from .mysql_view_models import MysqlViewTest
# Create your views here.


# def case_registration(request):
#     """案件登记"""
#     if request.method != 'POST':
#         form = MysqlViewModelsForm()
#     else:
#         print('&&&&&&&&&&&&&&&&&&&&&&&&')
#         form = MysqlViewModelsForm(request.POST)
#         if form.is_valid():
#             form.save()
#         for a in form:
#             print('<<<<<<<<')
#             print(type(a))
#             print(a)
#             print(')))))))))')
#         print('**********************')
#         return HttpResponseRedirect(reverse('make_document:dis_people'))
#     context = {'form': form}
#     return render(request, 'make_document/case_registration.html', context)


# def mysql_view_test(request):
#     """视图显示测试"""
#     tempa = MysqlViewTest.objects.all()
#     data = serializers.serialize("json", tempa)
#     return HttpResponse(data)


def index(request):
    """法律文书自动生成系统主  页"""
    return render(request, 'make_document/index.html')


@login_required()
def dis_people(request):
    """显示当事人信息"""
    # 获取people的所有对象
    people = NaturalPerson.objects.all().order_by('date_added')
    # 将要显示的数据装入分页器，以及确定每页多少行
    paginator = Paginator(people, 8)
    # 获取数据的页码数
    pag_num = paginator.num_pages
    # 获取当前页码，默认为1
    curuent_page_num = int(request.GET.get('page', 1))
    # 获取当前页的数据
    curuent_page = paginator.page(curuent_page_num)

    # 判断当前页是否小于11个
    if pag_num < 11:
        pag_range = paginator.page_range
    elif pag_num > 11:
        if curuent_page_num < 6:
            pag_range = range(1, 11)
        elif curuent_page_num > (paginator.num_pages-5):
            pag_range = range(pag_num-9, pag_num+1)
        else:
            # 当前页+5大于最大页数时
            pag_range = range(curuent_page_num-5, curuent_page_num+5)
    context = {'people': people, "pagintor": paginator, "current_Page": curuent_page,
                 "current_Page_num": curuent_page_num, "pag_range": pag_range,
               'people_num': paginator.count, 'page_num': paginator.num_pages}
    return render(request, 'make_document/dis_people.html', context)


@login_required()
def add_people(request):
    """增加当事人"""
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = NaturalPersonForm()
    else:
        form = NaturalPersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('make_document:dis_people'))
    context = {'form': form}
    return render(request, 'make_document/add_people.html', context)


@login_required()
def dis_enterprises(request):
    """显示违法企业信息"""
    # 获取people的所有对象
    enterprises = Enterprise.objects.all().order_by('date_added')
    # 将要显示的数据装入分页器，以及确定每页多少行
    paginator = Paginator(enterprises, 8)
    # 获取数据的页码数
    pag_num = paginator.num_pages
    # 获取当前页码，默认为1
    curuent_page_num = int(request.GET.get('page', 1))
    # 获取当前页的数据
    curuent_page = paginator.page(curuent_page_num)

    # 判断当前页是否小于11个
    if pag_num < 11:
        pag_range = paginator.page_range
    elif pag_num > 11:
        if curuent_page_num < 6:
            pag_range = range(1, 11)
        elif curuent_page_num > (paginator.num_pages-5):
            pag_range = range(pag_num-9, pag_num+1)
        else:
            # 当前页+5大于最大页数时
            pag_range = range(curuent_page_num-5, curuent_page_num+5)
    context = {'enterprise': enterprises, "pagintor": paginator, "current_Page": curuent_page,
                 "current_Page_num": curuent_page_num, "pag_range": pag_range,
               'enterprises_num': paginator.count, 'page_num': paginator.num_pages}
    return render(request, 'make_document/dis_enterprises.html', context)


@login_required()
def add_enterprise(request):
    """增加违法企业"""
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = EnterpriseForm()
    else:
        form = EnterpriseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('make_document:dis_enterprises'))
    context = {'form': form}
    return render(request, 'make_document/add_enterprise.html', context)


@login_required()
def del_people(request):
    """删除当事人"""


@login_required()
def update_people(request):
    """修改当事人"""

