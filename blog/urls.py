from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.show_category_posts)  # 카테고리로 가는 url
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),    // <자료형:변수명>
    # path('<int:pk>/', views.PostDetail)
    ]

# class PostList(ListView):
#     model = Post
#
# class PostDetail(DetailView):
#     model = Post