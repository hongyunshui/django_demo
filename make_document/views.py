from django.shortcuts import render

# Create your views here.


def index(request):
    """法律文书自动生成系统主  页"""
    return render(request, 'make_document/index.html')
