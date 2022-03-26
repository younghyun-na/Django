from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

# def index(request):
#
#     posts = Post.objects.all().order_by('-pk')   // 쿼리로 post 목록 가져오기 (역순으로)
#
#     return render(request,
#                   'blog/post_list.html',   // 사용할 템플릿
#                   {
#                       'posts': posts     // 템플릿에 넘겨줄 값 딕셔너리 형태로
#                   }
#                   )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk = pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post,
#         }
#     )

# ListView는 (모델명) _list.html을 템플릿으로 인지
class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post