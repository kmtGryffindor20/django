from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Views are made to connect the backend with the frontend and send/receive data between them
# They refer to some HTML tempelate.

# When using class based views we either need to name the templates as per convention
# Or we can use 'template_name' to change our default template name

# The data that these views send to the template is known as context
# In functional views we just send the context as dictionary of all accessed variables
# The templates can automatically access the User data

# In class based views the context is sent as 'object'. 
# The name of the object can be changed using 'context_object_name'

# When we need to define a view as LoginRequired we can use @login_required in functional views
# And LoginRequiredMixin inheritance in class based views

class PostListView(ListView):
    # Inside a class based view we need to tell which model/table the view is referring to
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # We can also give the fields in the model that need to be taken in when the view is Creating an object
    fields = ['title', 'content']

    #Overriding the Form Valid Method

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #Overriding the Form Valid Method

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # The 'test_func' function is required when we need to use the UserPassesTestMixin
    # So that we can check if the user is the correct user who has the access
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # When we are using a DeleteView we need to give a path where the web page will redirect to when the object is deleted
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
