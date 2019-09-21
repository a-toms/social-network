from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:username>', views.profile_view, name='profile'),
    path('add-friend/<int:sender_pk><int:recipient_pk>', views.add_friend_view, name='add-friend'),
]