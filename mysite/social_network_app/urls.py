from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:username>', views.profile_view, name='profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]