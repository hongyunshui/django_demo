from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import NaturalPerson
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


def index(request):
    """法律文书自动生成系统主  页"""
    return render(request, 'make_document/index.html')


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
                 "current_Page_num": curuent_page_num, "pag_range": pag_range}
    return render(request, 'make_document/dis_people.html', context)


def add_people(request):
    """增加当事人"""


def del_people(request):
    """删除当事人"""


def update_people(request):
    """修改当事人"""
