from django.shortcuts import render
from .models import CustomUser


def profile_view(request, username: str):
    user = CustomUser.objects.get(username=username)
    return render(request, 'social_network_app/profile.html', {'user': user})


def add_friend_view(request, sender_pk, recipient_pk):
    print(sender_pk, recipient_pk)
    return
