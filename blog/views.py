from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


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
    ordering = '-pk'

    # CBV에서 추가로 넘겨주고 싶은 context가 있을 때
    # 추가하고 싶은 요소를 context 딕셔너리에 담아 템플릿으로 보내기
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context


def show_category_posts(request, slug):
    # 미분류로 갈 링크
    if slug == 'no-category':
        category = "미분류"
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    context = {
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'category': category,
        'post_list': post_list
    }

    return render(
        request,
        'blog/post_list.html',
        context
    )

