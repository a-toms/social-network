from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',),
        error_messages={
            'unique': ("A user with that username already exists.",),
        },
    )
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    friends = models.ManyToManyField('self')

    def __str__(self) -> str:
        return str(self.username)


class Post(models.Model):
    text = models.CharField(max_length=600)
    datetime_posted = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=600)
    datetime_posted = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)






