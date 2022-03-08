from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkill =  profile.skill_set.exclude(description__exact="")
    otherSKill = profile.skill_set.filter(description="")
    context = {
        'profile': profile,
        'topSkill': topSkill,
        'otherSKill': otherSKill
    }
    return render(request, 'users/user_profile.html', context)
