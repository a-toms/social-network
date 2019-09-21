Create django project and django app

What is a web page? 4mins
What is a web app? 4mins


Brave, Chrome, or Firefox

TD Notes
- Expect spelling mistakes from the participants

1. Add app to the site-level settings
1.1 Open ```mysite/mysite/settings.py```
2. Update your INSTALLED_APPS to read:

``
INSTALLED_APPS = [
    'social_network_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
``

2.Create custom user
2.1.Create custom user in models.py
``
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

    def __str__(self) -> str:
        return self.username
``

2.2. Update ```mysite/mysite/settings.py```
Add ```AUTH_USER_MODEL = 'social_network_app.CustomUser'``` on a new line at the bottom
of the file.

2.3. Create migrations and migrate
run ```cd sn/mysite/``
run ```python manage.py makemigrations --dry-run``` # This command shows what migrations would be made.

You should see something like:
```
Migrations for 'social_network_app':
  social_network_app/migrations/0001_initial.py
    - Create model CustomUser
```

Then create the migrations and then migrate those created migrates to your database.
```python manage.py makemigrations -n adding_CustomUser```
```python manage.py migrate```

This will migrate the migration that you have just made, and will migrate the pre-built 
initial migrations that Django creates when you create a new project.






3. Create template to display the user on a page
The templates structure the HTML pages that your visitors will see in their browsers.

3.1 -> Create the folder structure and the template html file
cd mysite/social_network_app/  # Change directory
mkdir templates  # Creates the folder
cd mysite/social_network_app/templates # Change directory
mkdir social_network_app # Creates the folder
cd mysite/social_network_app/templates/social_network_app # Change directory
touch profile.html # Create a file called profile.html

3.2 -> Add HTML to the template
Paste the below HTML into profile.html. Replace anything that profile.html contained previously.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Profile</title>
</head>
<body>
<div>
    <nav>
        <h1>The Social Network</h1>
    </nav>
    <hr>
    <div>
        <img src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1280&h=300&fit=crop&ixid=eyJhcHBfaWQiOjF9"
             alt="Cover picture image not found"
        />
        <hr>
    </div>

    <h2>
        First name Last name
    </h2>
    <div>
        <p>Username:</p>
        <p>Email address:</p>
    </div>
</div>

</body>
</html>
```


4. Send information from your database to the template using a view.

4.1 -> Create a view 
views will send information from your database to your templates.

open ```social_network_app/views.py```
update the file so that it reads:
```
from django.shortcuts import render


def profile_view(request):
    return render(request, 'social_network_app/profile.html', {})
```

5. Add a url routing 
Adding a url routing will provide an address for your user to visit the page that views.py 
and your template create.

5.1 -> Add a url route for your site
cd sn/mysite/mysite
open urls.py
update your file so that it reads:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-network/', include('social_network_app.urls')),
]
```

5.2 -> Add a url route for your social network app

cd sn/mysite/social_network_app
touch urls.py  # Create urls.py
open urls.py
update the file so that it reads:
```
from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
]
```

5.3 -> Run your server and visit your created page!
cd sn/mysite/
python manage.py runserver
open your browser at the given url # This address will be http://127.0.0.1:8000/social-network/profile/
observe your web app's page!
 













User image:

    <img src="https://images.unsplash.com/photo-1511485977113-f34c92461ad9?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=300&h=300&fit=crop&ixid=eyJhcHBfaWQiOjF9"
         alt="profile picture image not found"
         />





