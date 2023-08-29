from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


# Here we define all our models.
# A model is like a table in SQL.
# Thus Post here is storing data regarding the Posts in the blog app 

class Post(models.Model):

    # In the model we need to define our Schema.
    # The attributes must be made through the models class from django.db

    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # A Foreign key relation can also be defines.
    # Here author_id is created which references the primary key of User model.
    # The User model is already created by django
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # This is to define where the browser should go when a change has been made and saved in the model throug the frontend
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.pk})
    

# We should register our model on the admin.py and should run the makemigrations and migrate command from manage.py