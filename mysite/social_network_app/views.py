from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def profile_view(request, username: str):
    user = CustomUser.objects.get(username=username)
    return render(request, 'social_network_app/profile.html', {'user': user})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            return redirect('profile', username)
        else:
            return redirect('login')

    else:  #  This covers the situation whereby the request.method == 'GET'.
        if request.user.is_authenticated:
            return redirect('profile', request.user.username)
        else:
            return render(request, 'social_network_app/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def add_friend_view(request, sender_pk, recipient_pk):
    sender = CustomUser.objects.get(pk=sender_pk)
    recipient = CustomUser.objects.get(pk=recipient_pk)
    sender.friends.add(recipient)
    return HttpResponse('<div>Test</div>')
