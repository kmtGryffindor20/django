from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Here we design the forms we require in our 'users' app

class UserRegisterForm(UserCreationForm):
    # The UserCreationForm provides automatic saving facility to the Users model
    email = forms.EmailField(required=False)

    # In here we can define many things regarding our ModelForm
    class Meta:
        # model define the Model we are using with this form
        model = User
        # fields define which fields from the inherited form do we want
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        # Here we are using ModelForm.
        # The fields are from the model we have specified
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']