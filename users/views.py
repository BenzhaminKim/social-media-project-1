from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileUpdateForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}!'.format(username) )
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html',{'form' : form})

@login_required
def profile(request):
    context = {
        'profile':Profile.objects.all()
    }
    return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm( request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,f'your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile_edit.html', {'p_form' : p_form})
