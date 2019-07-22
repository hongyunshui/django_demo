# from django.http import Http404
#
# from django_project01.app01.models import Topic
#
#
# def no_own_no_use(f):
#     def wrapper(request, topic_id):
#         topic = Topic.objects.get(id=topic_id)
#         # 禁止非拥有者访问主题
#         if topic.owner != request.user:
#             raise Http404
#         f(request, topic_id)
#
#     return wrapper
