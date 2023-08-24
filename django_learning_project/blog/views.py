from django.shortcuts import render

posts = [
    {
        'author': 'KMT',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Aug 24, 2018'
    },
    {
        'author': 'Kaustubh',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Aug 22, 2018'
    }
    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
