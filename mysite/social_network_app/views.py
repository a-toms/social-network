from django.shortcuts import render, redirect
from .models import CustomUser, Post
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PostForm

@login_required
def profile_view(request, username: str):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            if text != '':
                Post.objects.create(author=request.user, text=text)
        return redirect('profile', username=username)
    elif request.method == 'GET':
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


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def add_friend_view(request):
    if request.method == 'POST':
        sender_pk = request.POST['current_user_pk']
        recipient_pk = request.POST['profile_user_pk']
        sender = CustomUser.objects.get(pk=sender_pk)
        recipient = CustomUser.objects.get(pk=recipient_pk)
        sender.friends.add(recipient)
        return HttpResponse(status=200)


def signup_view(request):
    if request.method == 'POST':
        CustomUser.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],

        )
        return redirect('login')
    else:
        return render(request, 'social_network_app/signup.html')

@login_required
def feed_view(request):
    if request.method == 'GET':
        user = CustomUser.objects.get(username=request.user.username)  # Get the CustomUser instance of the current user.
        user_posts = Post.objects.filter(author=user)  # Get the user's posts from the database.
        print(user, user_posts)
        friends_posts = Post.objects.filter(author__in=user.friends.all())  # Get the user's friends posts from the database.
        feed_posts = user_posts | friends_posts  # Merge user_posts and friends_posts.
        return render(request, 'social_network_app/feed.html', {'feed_posts': feed_posts})  # Render the template and send the feed posts to the template.
