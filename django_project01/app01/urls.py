"""定义app01的URL模式"""
from django.conf.urls import url
from . import views

app_name = 'app01'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url('topics', views.topics, name='topics'),

    # 显示每个主题的详细情况
    url('topic/(?P<topic_id>\d+)', views.topic, name='topic'),

    # 用于添加新主题的网页
    url('new_topic/', views.new_topic, name='new_topic'),

    # 用于添加新条目的页面
    url('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),

    # 用于修改条目的页面
    url('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),

]
