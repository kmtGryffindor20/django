from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
