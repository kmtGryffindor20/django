from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    # If we get into the register route after a POST request.
    # We need to fill in the form with the prefilled data
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # And if the form data was valid, i.e, it follows the integrity constraints of the model it refers to.
        # We save the data into that model 
        if form.is_valid():
            print("X")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            # And should redirect to another meaningful page
            return redirect('login')
    else:
        # If we did not get a POST request, we simply show the empty form for the user to fill
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    # The profile page must only be accessible when the user is logged in and that's what the decorator is doing.

    # Same logic behind the two different Form creations
    if request.method == 'POST':
        # Here the instance of the form represents the object of the model the form refers to.
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        # If the form has files to be filled, we can use 'request.FILES' to access them
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, "Profile Update!")
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    # The context that needs to be sent to the corresponsing view is a dict
    context = {
        'u_form': user_update_form,
        'p_form': profile_update_form
    }

    return render(request, 'users/profile.html', context=context)