from django.shortcuts import render
from blog.models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
