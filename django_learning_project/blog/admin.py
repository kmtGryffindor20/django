from django.contrib import admin
from blog.models import Post
# Register your models here.

# When we have made our model we should register it on our site
admin.site.register(Post)