from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm


def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkill = profile.skill_set.exclude(description__exact="")
    otherSKill = profile.skill_set.filter(description="")
    context = {
        'profile': profile,
        'topSkill': topSkill,
        'otherSKill': otherSKill
    }
    return render(request, 'users/user_profile.html', context)


def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {
        'page': page
    }
    return render(request, 'users/login_register.html', context)


def register_page(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'You have successfully registered!')
            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'An error has occured during registration')

    context = {
        'page': page,
        'form': form
    }
    return render(request, 'users/login_register.html', context)


def logout_page(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('login')
