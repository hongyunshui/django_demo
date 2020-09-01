"""定义make_document的URL模式"""
from django.conf.urls import url
from . import views
app_name = 'make_document'

urlpatterns = [
    # 显示已制作案件页面
    url(r'^$', views.index, name='index'),

    # 显示所有人员
    url('dis_people', views.dis_people, name='dis_people'),

    # 增加当事人
    url('add_people', views.add_people, name='add_people'),

]
