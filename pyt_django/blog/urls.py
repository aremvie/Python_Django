#20200806- Add UserPostListView
from django.urls import path #TUT1
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


urlpatterns = [
    #path('', views.home, name='blog-home'), #replaced with PostListView, TUT1
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # then create post_detail under template
    path('post/new/', PostCreateView.as_view(), name='post-create'), #822020share with update template(blog_form.html)/ then views.py
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # 822020_from views then add UserPassesTestMixin
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # 822020_from views delete post then create post_delete.html
    path('about/', views.about, name='blog-about'),
]