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

    # # 视图测试
    # url('mysql_view_test', views.mysql_view_test, name='mysql_view_test'),
    #
    # # 案件登记
    # url('case_registration', views.case_registration, name='case_registration'),

]
