from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    templete_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
