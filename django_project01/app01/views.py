from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """学习笔记的主页"""
    return render(request, 'app01/index.html')


@login_required
def topics(request):
    """显示所有主题"""
    # topics = Topic.objects.order_by('date_added')
    # 只显示拥有者自己的主题
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'app01/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题及所有条目"""
    topic = Topic.objects.get(id=topic_id)
    # 禁止非拥有者访问主题
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'app01/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据创建一个新表单
        form = TopicForm()
    else:
        # POST 提交数据，对数据进行处理
        form = TopicForm(request.POST)
        # form.is_valid()函数用来确认已经填写了必不可少的字段，且输入的数据与要求的字段类型一致
        if form.is_valid():
            new_topic = form.save(commit=False)
            # 把提交数据的用户信息给新的topic的owner属性
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('app01:topics'))
    context = {'form': form}
    return render(request, 'app01/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    # 禁止其它用户恶意增加条目
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 未提交数据创建一个新表单
        form = EntryForm()
    else:
        # POST 提交数据，对数据进行处理
        form = EntryForm(data=request.POST)
        # form.is_valid()函数用来确认已经填写了必不可少的字段，且输入的数据与要求的字段类型一致
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('app01:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'app01/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # 禁止非拥有者修改条目
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST 提交数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app01:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'app01/edit_entry.html', context)


if __name__ == "__main__":
    print("main test")
