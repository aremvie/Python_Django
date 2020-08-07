#20200806-Add pagination at class PostListView(ListView):
#20200806-Added Filter the post by user, add import get_object_or_404 and from django.contrib.auth.models import User
#20200806-Added Filter-create path to url pattern, create user_posts, then modify link on home and post_detail
from django.shortcuts import render, get_object_or_404 #TUT1
from django.http import HttpResponse #TUT1
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
# TUT1

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
# TUT1
class PostDetailView(DetailView): #posting individual article, then create url pattern (urls.py)
    model = Post

#creating post
# added "LoginRequiredMixin" on the parameter to redirect user to login page when creating post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # 822020_from urls
    def form_valid(self, form):
        form.instance.author=self.request.user #set the author as the current logged in user
        return super().form_valid(form)
# 822020_add UserPassesTestMixin on the parameter
#UserPassesTestMixin to avoid some one to edit your post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author=self.request.user #set the author as the current logged in user
        return super().form_valid(form)

# 822020_from urls then go to blog models then create reverse function
#check if the current logged in use is the author of the post
    def test_func(self): #goes with UserPassesTestMixin
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

# 822020_Update view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/' #redirecting to home page after deleting a post
# check if the current logged in use is the author of the post
    def test_func(self): #goes with UserPassesTestMixin
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app> / <model>_<viewtype>.html
    context_object_name = 'posts'  # as written in def home, w/o this no post will be shown
    ordering = ['-date_posted'] # order of post
    paginate_by = 5 #8062020-limit the post appeared to specified number(post==3)


#20200806-Filter the post by user-START
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    #ordering = ['-date_posted']  #moved the ordering to def get_query
    paginate_by = 5

    def get_queryset(self):
        user =get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

#20200806-Filter the post by user the create path to url pattern-END
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
