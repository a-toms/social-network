<a href="https://codeclimate.com/github/a-toms/social-network/maintainability"><img src="https://api.codeclimate.com/v1/badges/d21b1f506d904315edae/maintainability" /></a>

Create a Social Network with Django!
--

Introduction explanation by Tom:
- What is a web page? 
- What is a web app? 
- What is Django? 
- What is the Django ORM?


*Tutorial*
-
First ensure that you have installed python (following the instructions at https://tutorial.djangogirls.org/en/installation/#virtual-environment)

Today's aim is to create a basic social network app that will run locally, and that you 
could easily expand and deploy online. 
The aim is not to understand everything, but to gain an impression of the process of
creating a web app, and to create a web app yourself by following my actions.

There are many web frameworks. Django is particularly robust, scalable, and has excellent
documentation. The process of creating an app with Django is similar to creating a web 
app with another web framework.


A. Install Django 
--

 - Open Pycharm Professional
 - Select File > New Project > Pure python
 - Open the terminal by selecting the terminal button in Pycharm
 (Tom explains virtual environment)
 - Into the terminal, enter ```pip install django```
 
B. Create Django Project
--
- In the terminal enter:
```django-admin startproject mysite```
- Then enter:```cd mysite```
- Then enter: ```django-admin startapp social_network_app```

Nice - You have just created the django site and the django app that 
will interact with the site.

- Run your server by entering the following into your terminal in the same directory
as ```manage.py```
```python manage.py runserver```
- Visit your installed django site! 

---
Now we will connect the app to the site:


1. Add app to the site-level settings by opening```mysite/mysite/settings.py```
2. In ````settings.py```` update your INSTALLED_APPS to read:

```
INSTALLED_APPS = [
    'social_network_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

<h3> Create your first model </h3>
Create your custom user:

- Open ```models.py```in ```mysite/social_network_app/``

- Create custom user in models.py by adding the below:
```
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
```

1. Update ```mysite/mysite/settings.py``` to recognise the new user model.
(Note that User models have special requirements in Django compared to other models)

- To do this, add ```AUTH_USER_MODEL = 'social_network_app.CustomUser'``` on a new line at the bottom
of your ```settings.py``` file.

3. Create migrations and migrate
- Move to your manage.py director: ```cd sn/mysite/``
- Run ```python manage.py makemigrations --dry-run```. This command shows what migrations would be made.

You should see something like:
```
Migrations for 'social_network_app':
  social_network_app/migrations/0001_initial.py
    - Create model CustomUser
```

- Then create the migrations for real and then migrate those created migrations to your database.
  - ```python manage.py makemigrations -n adding_CustomUser```
  - ```python manage.py migrate```

This will migrate the migration that you have just made, and will migrate the pre-built 
initial migrations that Django creates when you create a new project.

Create your first template
---
In Django, templates provide the structure for the HTML pages that your visitors will see in their browsers.

- Tom to explain briefly Django's overarching MVT structure. This involves models -> views -> templates 

To create your first template:

1 - Create the folder structure and the template html file:

 - ```cd mysite/social_network_app/```  # Change directory to your app
 - ```mkdir templates```  # Creates the templates folder
 - ```cd mysite/social_network_app/templates``` # Change directory
 - ```mkdir social_network_app``` # Creates the folder
 - ```cd mysite/social_network_app/templates/social_network_app``` # Change directory
 - ```touch profile.html`` # Create a file called profile.html

 2 - Add HTML to the template:
 
Paste the below HTML into your ```profile.html```. Replace anything that profile.html contained previously.
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
        Current user: {{request.user}}
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

3 - Now we will send information from your database to the template using a view.

3.1 - Create a view:
 
Django uses views to send the information from your database to your templates, 
and for you to retrieve information from your database.

To create your first view,
 - open ```mysite/social_network_app/views.py```
 - update the file so that it reads:
```
from django.shortcuts import render


def profile_view(request):
    return render(request, 'social_network_app/profile.html', {})
```

4 - Add a url routing:

Adding a url routing will provide an address for your user to visit the page that views.py 
and your template create.

4.1 - Add a url route for your <i>site</i> by entering:
```
cd /mysite/mysite/
open urls.py
```

- Update your ```mysite/urls.py``` file so that it reads:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-network/', include('social_network_app.urls')),
]
```

4.2 - Add a url route for your social network app profile


 - `cd /mysite/social_network_app`
 - `touch urls.py`  # Create urls.py
 - open urls.py
 - update the file so that it reads:
 
```
from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
]
```

5.3 -> Run your server and visit your created profile page!

`cd /mysite/`

`python manage.py runserver`

- Open your browser at the given url. This address will be http://127.0.0.1:8000/social-network/profile/
- Observe your web app's page!

Note: If you encounter a template error, it is likely that you have mispelled a path to the profile
template. If you encounter a page not found error, it is likely that you have mispelled the 
one or more of the urls.

---

Create an admin page for your app
--
We will now create a superuser via the terminal.
This superuser implements your CustomUser model that you defined in models.py.
We will create a superuser with special admin permissions below. We will create other users
in a simpler way later.

To create your first superuser, enter in your terminal:

- ```cd /mysite/```
- ```python manage.py createsuperuser```

Add the following details for the new superuser:
```
username=redmark
email=fast@mail.com
password=rocksalt1
```

Note that we could use any details for the above. However, I recommend using the 
above details to avoid unnecessary additional detail.
 
1 - Create an admin page and register your first model:

- ```cd sn/mysite/social_network_app/```
- Open admin.py
- Update the file so that it reads:

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.register(CustomUser, UserAdmin)
```

2 - Visit your site's admin page and login using your superuser's details.

Restart your server:

```cd /mysite/```

```python manage.py createsuperuser```

Visit ```http://127.0.0.1:8000/admin``` in your browser and enter your superuser's login details. 
Welcome to the django admin site! This automatically generated admin site provides 
a graphical user interface that you may use to create new model instances (e.g., CustomUsers).

- Click on 'Users'
- Click on 'add new User'
- Add the following details for the new user:
```
username=nightcat1
password=rocksalt1
```
- Click SAVE

- Then enter the following details for the user
```
first_name=(Enter your first name)
last_name=(Enter your last name)
email=fast@mail.com
```
- Then scroll down and click save.

Congratulations! You have just added a user to your database in accordance with the 
database structure that you defined earlier in models.py!



Create a profile page for our user
--

We will now set our app's ```urls.py``` to send the user's username in an url address to views.py

1. To add the new url route:
- Go to urls.py ```cd sn/mysite/social_network_app/urls.py```
- Update your file so that it reads:
```
from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:username>', views.profile_view, name='profile'),
]
```

2 -> Update your views to receive a user's username from the address.
To do this:

- Go to views.py ```cd /mysite/social_network_app/views.py```
- Update your views file so that it reads:
```
from django.shortcuts import render
from .models import CustomUser


def profile_view(request, username: str):
    user = CustomUser.objects.get(username=username)
    return render(request, 'social_network_app/profile.html', {'user': user})
```


3 - Update your template to use the data in the newly received user model instance to render the particular user's profile page.

To do this:
- Open your template at ``mysite/social_network_app/templates/social_network_app/profile.html``
- Update your file so that it contains:
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
        Current user: {{request.user}}
    </nav>
    <hr>
    <div>
        <img src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1280&h=300&fit=crop&ixid=eyJhcHBfaWQiOjF9"
             alt="Cover picture image not found"
        />
        <hr>
    </div>

    <h2>
        {{user.first_name}} {{user.last_name}} 
    </h2>
    <div>
        <p>Username: {{user.username}}</p>
        <p>Email address: {{user.email}}</p>
    </div>
</div>

</body>
</html>
```

Restart your server (```python manage.py runserver```) and visit your server at ```http://127.0.0.1:8000/social-network/profile/nightcat1```and refresh your page.
Nice job so far!

(If no change, check that your browser's caching is disabled in your browser's settings)

Login and Logout
--
We will now enable the user to login and to logout.
 
1  - To do this we will first, update the urls to create a login url address.


 - ```cd mysite/social_network_app/urls.py```
 - Update urls.py so that it  matches the below:
```
from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:username>', views.profile_view, name='profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout)',
]
```

2 - Create a login template
To do this we will:
 - Create a new file at ```mysite/social_network_app/templates/social_network_app/login.html```
 - Copy the below html into the file. Replace anything that is already in the file.
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>

<body>
<div>
    <form method="post">
        {% csrf_token %}
        <div>
            <label>
                <input placeholder="Username"
                       name="username"
                       type="text"
                       autocomplete="off"
                >
            </label>
        </div>
        <div>
            <label>
                <input placeholder="Password"
                       name="password"
                       type="password"
                       autocomplete="off"
                >
            </label>
        </div>
        <button class="btn" type="submit">
            Login
        </button>
    </form>
</div>
</body>
</html>
```


 - Update your profile template to add a logout button:
 
```cd mysite/social_network_app/templates/social_network_app/profile.html```


Update the ```profile.html``` so that it contains the below:

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
        Current user: {{request.user}}
        <a href="{% url 'logout' %}">
            <button>
                Logout
            </button>
        </a>
    </nav>
    <hr>
    <div>
        <img src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1280&h=300&fit=crop&ixid=eyJhcHBfaWQiOjF9"
             alt="Cover picture image not found"
        />
        <hr>
    </div>

    <h2>
        {{user.first_name}} {{user.last_name}}
    </h2>
    <div>
        <p>Username: {{user.username}}</p>
        <p>Email address: {{user.email}}</p>
    </div>
    <div>
        <div>
            <h3>
                Friends: None yet
            </h3>
        </div>
        <br>
    </div>
</div>

</body>
</html>
```


Now we will create a login view to interact with the login template
To do this we will:
 - Open ```views.py```
 - Update the our views.py to include the below:
```
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
```

We will now create a logout view that will allow the user to logout. 
- To do this, add the below at the end of views.py`:

```
def logout_view(request):
    logout(request)
    return redirect('login')
```

Now we will visit your user's profile page, logout, and login! To do this:
- Go to ```http://127.0.0.1:8000/social-network/profile/redmark```
- Press the logout button. 
- Notice that your app sends you to your newly created login page!
- Login again!  

TD Troubleshooting:
If you are unable to login, it is likely that: a) you have entered the wrong details, 
or b) you created your users with different login details than suggested above. 
To remedy this, follow the guidance earlier in the tutorial to create another user and 
try again with those details. Remember that we specified in `models.py that each 
user's username and email must be unique.



<h1>Part 2 - Make friends</h1>
---
We want to allow our users to add each other as friends. 


The link that we will use is called a 'Many to Many' connection. As the name implies,
a m2m field may connect many database entries to many other database entries.
Because each user's friends will be other users, we will create a m2m model that links to itself (a recursive connection).
(+ brief database connections explanation by Tom)


To do this we will first update your CustomUser model to create a field that links to other users. 

 1 - Update your `social_network_app/models.py` to include the following:

```
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
    friends = models.ManyToManyField('self')  # Add this line
    
    def __str__(self) -> str:
        return str(self.username)
```

2 - Now update your database by migrating your model changes with our trusty `manage.py`:

- ```cd /mysite/```
- ```python manage.py makemigrations -n add_friends_field_to_User```
- ```python manage.py migrate```

---

3 - Add html to your template that will show your friends:

Now let's update your profile template to:

a) show the user's name as the the current user, rather the user's username, and

b) show an 'add as friend' button if the profile is not the current user's profile

c) show each user's friends

Update template:
To do this: 
- Open your template at ```mysite/social_network_app/templates/social_network_app/profile.html```
- Update your file so that it contains:
```
<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <title>User Profile</title>
</head>

<body>
<div>
    <nav>
        <h1>The Social Network</h1>
        Current user: {{request.user.first_name}}
        <a href="{% url 'logout' %}">
            <button>
                Logout
            </button>
        </a>
    </nav>
    <hr>
    <div>
        <img src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1280&h=300&fit=crop&ixid=eyJhcHBfaWQiOjF9"
             alt="Cover picture image not found"
        />
        <hr>
    </div>

    <div>
        {{user.first_name}} {{user.last_name}}
        {% if request.user.pk != user.pk %}
            {% if request.user in user.friends.all %}
                <button>
                    Is a friend!
                </button>
            {% else %}
                <button id="add-friend-button">
                    Add as friend
                </button>
            {% endif %}
        {% endif %}
    </div>
    <div>
        <p>Username: {{user.username}}</p>
        <p>Email address: {{user.email}}</p>
    </div>
    <div>
        <div>
            <h3>Friends:</h3>
            {% if user.friends.all %}
                {% for friend in user.friends.all %}
                    <p>{{friend.username}}</p>
                {% endfor %}
            {% else %}
                <p>No friends yet</p>
            {% endif %}
        </div>
        <br>
    </div>

</div>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
        crossorigin="anonymous">
</script>
<script type="text/javascript"
        src="{% static 'social_network_app/js/profile.js' %}">
</script>

<script>
    const csrfToken = '{{ csrf_token }}';
    addClickListenerToAddFriendButton({{request.user.pk}}, {{user.pk}}, csrfToken);
</script>

</body>
</html>
```
---
-> Create a new view:

Next, we will create a new view that that we may use to add someone as a friend.
To do this:
- Open views.py
- Add the below view to the bottom of our `views.py` file:

```
def add_friend_view(request):
    if request.method == 'POST':
        sender_pk = request.POST['current_user_pk']
        recipient_pk = request.POST['profile_user_pk']
        sender = CustomUser.objects.get(pk=sender_pk)
        recipient = CustomUser.objects.get(pk=recipient_pk)
        sender.friends.add(recipient)
        return HttpResponse(status=200)
```

-> Create a new url route
Now we will add a new url route to the new view. To do this,
- Update your app's urls.py at ```social_network_app/urls.py```:

```
urlpatterns = [
    ...
    path('add-friend/', views.add_friend_view, name='add-friend'),
]
```

---
<h3>Adding our first javascript!</h3>

Now we want to add the ability to press the button to add a person as a friend without leaving the page.

We want to be able to press the 'Add as friend' button to add a friend without leaving or refreshing the entire 
profile page. To do this, we will run a script on part of the page when we click the button. 
More specifically, we will use javascript to make an asynchronous call to our 'add_friend_view' in ```views.py```.

Note : One way to make this async call cleaner is to use a javascript library called 'Intercooler JS' that
I and a few friends like using. However, we will use javascript with jquery (another js library) in
this tutorial. The Jquery method involves less setup than using Intercooler JS and is clearer
on first glance to a less experienced eye. However, I recommend using Intercooler JS for future javascript projects.

To add javascript to our button:
- First, create a suitable directory structure for your javascript files

```mkdir mysite/social_network_app/static/```

```mkdir mysite/social_network_app/static/social_network_app```
- Create a javascript file called `profile.js``

```touch mysite/social_network_app/static/social_network_app/profile.js```
- Open file and add the following javascript:
```

function addClickListenerToAddFriendButton(currentUserPk, profileUserPk, token) {
    const addFriendButton = document.querySelector('#add-friend-button');
    addFriendButton.addEventListener('click', () => {
        $.ajax({
            type: "POST",
            url: "/social-network/add-friend/",
            data: {
                'current_user_pk': currentUserPk,
                'profile_user_pk':profileUserPk,
                'csrfmiddlewaretoken': token
            },
            dataType: "html",
            success: function (response) {
                addFriendButton.textContent = 'Added';
            },
        })
    })
}
```
The above javascript and jquery:
- Gets the DOM element button (addFriendButton)
- Adds an event listener that fires an ajax call when the user clicks the button.
- This ajax call sends the primary key (pk) of the user who was visiting the page - which we
have named the 'currentUserPk' - and the pk of the user whose profile the current user is visitind - 
which we have called 'profileUserPk' - in a json format in the parameters of the POST request to 
"/social-network/add-friend/"
- When the data arrives at "/social-network/add-friend/", ```urls.py``` routes the data to 
the ```add_friend_view``` function in ```views.py```
- Our ```add_friend_view``` function then retrieves both users from the database, and adds 
our friend many to many connection between the two users
- The profile template then updates the page html.


Create signup page
--

To create a signup page, we will follow a similar approach as previously.

1 - Create a signup template file:
- ```cd mysite/social_network_app/templates/social_network_app```
- ```touch mysite/social_network_app/templates/social_network_app/signup.html```

When a person signs up, we must allow the person to provide the information that our
CustomUser model requires to create an instance of that CustomUser model in our database.

We will send that allow the person to send this required information to us by using forms
in our html. 

To do this, add the following html to ``signup.html``:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Signup</title>
</head>
<body>
<nav>
    <h1>The Social Network</h1>
</nav>
<form>
    <div>
        <input type="text" name="first_name" placeholder="First name">
    </div>
    <br>
    <div>
        <input type="text" name="last_name" placeholder="Last name">
    </div>
    <br>
    <div>
        <input type="text" name="username" placeholder="Username">
    </div>
    <br>
    <div>
        <input type="password" name="password" placeholder="Password">
    </div>
    <br>
    <div>
        <input type="email" name="email" placeholder="Email">
    </div>
    <button type="submit">
        Sign up!
    </button>
</form>

</body>
</html>
```

2 -  As before, we will then create a view that will send data to our template.
To do this, 
- In your views.py, add the below:
```
def signup_view(request):
    if request.method == 'POST':
        CustomUser.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        return redirect('login')
    else:
        return render(request, 'social_network_app/signup.html')
```

3 - Create an url address to route to our view:

To do this:
 - in urls.py, add the following to our url patterns
(Ignore the ellipses. The ellipses represent the paths that we have already added):
```
urlpatterns = [
	...
    path('signup/', views.signup_view, name='signup'),
]
```

4 -  Visit your signup page!

- Run your server if it is not already running by entering:
  - ```cd sn/mysite/```
  - ```python manage.py runserver```
- Visit your signup page
- Create a new user
- Log in!


5 -  Update views.py to require any visitor to login before visiting a profile page

Issue: Currently, any visitor to the page can visit any profile, regardless
of whether that visitor is logged in. We will update our views.py to require a 
login.

To do the above, we will use a python construct called 'decorators'. Django provides 
pre-built login decorators. 

We will add these login decorators to our views that 
require a login. This will involve making each of our views require a logged in user,
besides the login view and the signup view.

To do this:
- update your views.py so that your code looks like:

```
from django.shortcuts import render, redirect
from .models import CustomUser, Post
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required    # Added

@login_required	# Added
def profile_view(request, username: str):
    if request.method == 'POST':
        if request.POST['text']:
            text = request.POST['text']
            Post.objects.create(
                author=request.user,
                text=text
            )
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


@login_required  # Added
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required  # Added
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
            email=request.POST['email']
        )
        return redirect('login')
    else:
        return render(request, 'social_network_app/signup.html')
```

Update settings.py:
We will add the below two lines to the bottom of your ```settings.py```file. This will redirect the user after he or she logs in.

To do this:
- open settings.py at ```cd social-network/mysite/mysite/```
- add the below to the bottom of settings.py:
```
# Custom login url and login redirect.
# This is included to redirect the session to the login page if there is not a
# logged in user.
LOGIN_URL = '/social-network/login/'
LOGIN_REDIRECT_URL = '/social-network/'
```
--

Styling!
--
Now we will add some styling using CSS! (Tom will briefly explain CSS)

1. To prepare your template for the styling:
- update your profile template so that it contains the following:
```
<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link rel="stylesheet" type="text/css" href="{% static 'social_network_app/css/profile.css' %}">
    <link href="https://fonts.googleapis.com/css?family=Vollkorn+SC&display=swap" rel="stylesheet">

    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <meta charset="UTF-8">
    <title>User Profile</title>
</head>

<body>
<nav>
    <div class="nav-wrapper">
        <a href="#" class="brand-logo">The Social Network</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href=""></a></li>
            {% if request.user.username %}
                <li><a href="{% url 'profile' username=request.user.username %}">{{ request.user.first_name }}</a></li>
            {% else %}
                <li><a href="">Guest</a></li>
            {% endif %}
            <li><a href="{% url 'logout' %}"><i class="material-icons">exit_to_app</i></a>
                Logout
            </li>
        </ul>
    </div>
</nav>

<div class="card top-container">
    <div class="card-image waves-effect waves-block waves-light cover-photo-container">
        <img class="cover-photo"
             src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&fit=crop&ixid=eyJhcHBfaWQiOjF9"
             alt="Cover picture image not found"
        >
    </div>
    <div class="profile-picture-container card-content">
           <div class="">
<img src="https://images.unsplash.com/photo-1555964840-87d32a60e722?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=540&h=406&fit=crop&ixid=eyJhcHBfaWQiOjF9" 
alt="" class="circle responsive-img profile-picture">
<!-- notice the "circle" class -->
           <div class="profile-name grey-text ">
               {{ user.first_name }} {{ user.last_name }}
           </div>
               <div class="personal-details grey-text text-darken-5">
                   <p><i>{{ user.email }}</i></p>
                   <p><i>{{ user.username }}</i></p>
               </div>
               <div class="right add-friend-container">
                    {% if request.user.pk != user.pk %}
                        {% if request.user in user.friends.all %}
                            <button>
                        Is a friend! <i class="material-icons">person</i>
                            </button>
                        {% else %}
                            <button type="button" class="btn waves-effect waves-light blue" id="add-friend-button">
                                <i class="material-icons">person_add</i>
                            Add friend
                            </button>
                        {% endif %}
                    {% endif %}
                </div>

            <div>

            </div>
        </div>
    </div>
    <div class="section-container">

    </div>
    <div class="section-container">
        <div class="column-container-1">
            <div class="column-container-1-item-size-one">
                <div class="section-title">
                    Interests
                    <div class="section-text">
                        <p>Rock sailing
                            Water hiking
                            Pit jumping
                            Forest rafting
                            Loud Shouting
                        </p>
                    </div>
                </div>
                <div class="section-title">Friends
                    <i class="material-icons friends-icon">group</i>
                </div>
                {% if user.friends.all %}
                    {% for friend in user.friends.all %}
                        <a href="{% url 'profile' username=friend.username %}">
                            <div class="row valign-wrapper current-friend-container">
                                <button type="submit">
                                    <div class="current-friend-card">
                                        <img src="http://source.unsplash.com/E_h1wome8Jc/540x406" alt="" class="responsive-img">
                                        <div class="black-text">
                                            {{ friend.first_name }} {{ friend.last_name }}
                                        </div>
                                    </div>
                                </button>
                            </div>
                        </a>
                    {% endfor %}
                {% else %}
                    <p>No friends yet</p>
                {% endif %}
            </div>

            <div class="column-container-1-item-size-two">
                <div class="section-title">
                    New post
                </div>
                <div>
                    <div class="input-field col ">
                        <textarea id="textarea2" class="materialize-textarea"></textarea>
                        <label for="textarea2"></label>
                    </div>
                    <button class="right">Post</button>
                </div>
                <div class="section-title">
                    wall
                </div>
                <div>
                    {% lorem 100 w %}
                </div>
            </div>
        </div>
    </div>

</div>

<script src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
        crossorigin="anonymous">
</script>
<script type="text/javascript"
        src="{% static 'social_network_app/js/profile.js' %}">
</script>
<!-- Compiled and minified JavaScript -->


<script>
    const csrfToken = '{{ csrf_token }}';
    const currentUser = '{{request.user.pk}}';
    if (currentUser) {
        addClickListenerToAddFriendButton(currentUser, {{user.pk}}, csrfToken);
    }
</script>

</body>
</html>
```

2 -  Add CSS to style your profile page.
To do this:
- ```cd mysite/social_network_app/static/```
- Make a new directory: ```mkdir mysite/social_network_app/static/social_network_app/css```
- Make a new CSS file called profile.css: ```touch mysite/social_network_app/static/social_network_app/css/profile.css```
- Copy and paste the following CSS into ```profile.css```:
```
body {
    background: #fffcfc;
}

img {
    max-width: 100%;
    height: 300px;
    border: 2px solid rgba(111, 59, 148, 0.13);
}

body {
    background-image: linear-gradient(to right, rgba(29, 112, 255, 0.31));
}


.nav-bar {
    display: flex;
    width: 100%;
    height: 100%;
}

.box {
    text-align: center;
    justify-content: center;
    align-self: center;
    flex: 1;
}

.nav-element {
    font-size: 24px;
}


.site-title {
    flex: 1;
}

.current-user {
    flex: 1;
}

.top-container {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 75%;
    z-index: -1;
    position: absolute !important;
    left: 0;
    right: 0;
}

.cover-photo-container{
    width: 100%;
}


.cover-photo {
    display: block;
    border-radius: 2px 2px 0 0;
    object-fit: cover;
    bottom: 0;
}

.card {
    position: absolute;
    background-color: #fff;
    -webkit-transition: -webkit-box-shadow .25s;
    transition: -webkit-box-shadow .25s;
    border-radius: 2px;
}
.card-image {
    top: -60px
}

.card-content {
    padding-top: 24px;
    padding-left: 24px;
    padding-right: 24px;
    padding-bottom: 10px;
}


.profile-picture-container {
    border: 3px solid white;
    box-shadow: 0px 0px 2px 2px lightgrey;
    z-index: 1;
    position: relative;
}


.profile-name{
    margin-left: 13rem;
    margin-top: -7rem;
    margin-bottom: 5em;
    font-size: 24px;
}

.personal-details {
    margin-left: 13rem;
    margin-top: -8rem;
    font-size: 16px;
    padding-bottom: 20px;
}


.add-friend-container {
    margin-top: -9rem;
}

#add-friend-button {
    font-size: 13px;
    border-radius: 3px;
}


.body-container{
    display: flex;
    flex-direction: column;
}

.container {
    flex: 1;
    flex-direction: column;
}

.column-item{
    flex: 1;
    width: 33%;
}

.section-title {
    font-size: 2.92rem;
    line-height: 80%;
    margin: 1.9466666667rem 0 1.168rem 0;
}

.section-text {
    font-size: 16px;
}

.btn {
    cursor: pointer;
}

.column-container-1 {
    display: flex;
    width: 95%;
    text-align: left;
    margin: auto;
}

.column-container-1-item-size-one {
    flex: 1;
}

.column-container-1-item-size-two {
    flex: 2;
}

.friends-icon{
    font-size: 35px !important;
}

.current-friend-container{
    display: flex;
    justify-content: left;
    align-items: center;
}

textarea.materialize-textarea {
    line-height: normal;
    overflow-y: hidden;
    padding: .8rem 0 .8rem 0;
    min-height: 6rem;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
}

```

Great job so far! The social network app is starting to look good.


<h1>Add Posts</h1>
---
We will now dd a "New Post" section to the html in your profile page
This will include a form with a text area and a button that you will press to create a 
new post.

We will first add a Post models to your models.py. We will now create the models to define each post in 
your database. As with your CustomUser model above, we will then send this
data to your template.

We will add a Post model to models.py
```cd models.py```

To do this:
- At the bottom of your `models.py`, below your CustomUser model, add the following to create the Post:
```
class Post(models.Model):
    text = models.CharField(max_length=600)
    datetime_posted = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ['-datetime_posted']
 
```

- Underneath the Post mode, add a Comment model:
```
class Comment(models.Model):
    text = models.TextField(max_length=600)
    datetime_posted = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
```

We will now make migrations and then migrate. To do this,
- ```cd sn/mysite```
- To check the migrations, enter:```python manage.py makemigrations --dry-run``` 
You should see an output similar to:
```
Migrations for 'social_network_app':
  social_network_app/migrations/0003_comment_post.py
    - Create model Post
    - Create model Comment
```
If your output is similar to the above, make the migrations and then migrate by entering
- ```python manage.py makemigrations -n added_Post_and_Comment_models```
- ```python manage.py migrate```


3 - We will now create forms.py to receive your data
- ```cd mysite/social_network_app/```
- ```touch forms.py``` # Create forms.py

- Add the following to your `forms.py` file:
```
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
```

---

4 -  We will now show the posts for each post in your user's profile
The app will show a user's posts on the user's profile page where that user was the author of the 
post.

To do this,
- First, update your profile view in your views.py to process the newly received data from the html 
template. Update your profile view to accord with the below:

In `views.py`:
```
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
```


- Then update your template to show the posts that each user has posted on their
profile! 
Update your `profile.html` template so that it contains the below:

```
<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link rel="stylesheet" type="text/css" href="{% static 'social_network_app/css/profile.css' %}">
    <link href="https://fonts.googleapis.com/css?family=Vollkorn+SC&display=swap" rel="stylesheet">

    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <meta charset="UTF-8">
    <title>User Profile</title>
</head>

<body>
<nav>
    <div class="nav-wrapper">
        <a href="#" class="brand-logo">The Social Network</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href=""></a></li>
            {% if request.user.username %}
                <li><a href="{% url 'profile' username=request.user.username %}">{{ request.user.first_name }}</a></li>
            {% else %}
                <li><a href="">Guest</a></li>
            {% endif %}
            <li><a href="{% url 'logout' %}"><i class="material-icons">exit_to_app</i></a>
                Logout
            </li>
        </ul>
    </div>
</nav>

<div class="card top-container">
    <div class="card-image waves-effect waves-block waves-light cover-photo-container">
        <img class="cover-photo"
             src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&fit=crop&ixid=eyJhcHBfaWQiOjF9"
             alt="Cover picture image not found"
        >
    </div>
    <div class="profile-picture-container card-content">
           <div class="">
<img src="http://source.unsplash.com/E_h1wome8Jc/540x406" alt="" class="circle responsive-img profile-picture">
<!-- notice the "circle" class -->
           <div class="profile-name grey-text ">
               {{ user.first_name }} {{ user.last_name }}
           </div>
               <div class="personal-details grey-text text-darken-5">
                   <p><i>{{ user.email }}</i></p>
                   <p><i>{{ user.username }}</i></p>
               </div>
               <div class="right add-friend-container">
                    {% if request.user.pk != user.pk %}
                        {% if request.user in user.friends.all %}
                            <button type="button" class="btn waves-effect waves-light pink">
                                Is a friend <i class="material-icons">person</i>
                            </button>
                        {% else %}
                            <button type="button" class="btn waves-effect waves-light blue" id="add-friend-button">
                                <i class="material-icons">person_add</i>
                            Add friend
                            </button>
                        {% endif %}
                    {% endif %}
                </div>

            <div>

            </div>
        </div>
    </div>
    <div class="section-container">

    </div>
    <div class="section-container">
        <div class="column-container-1">
            <div class="column-container-1-item-size-one">
                <div class="section-title">
                    Interests
                    <div class="section-text">
                        <p>Rock sailing
                            Water hiking
                            Pit jumping
                            Forest rafting
                            Loud Shouting
                        </p>
                    </div>
                </div>
                <div class="section-title">Friends
                    <i class="material-icons friends-icon">group</i>
                </div>
                {% if user.friends.all %}
                    {% for friend in user.friends.all %}
                        <a href="{% url 'profile' username=friend.username %}">
                            <div class="row valign-wrapper current-friend-container">
                                <button type="submit">
                                    <div class="current-friend-card">
                                        <img src="http://source.unsplash.com/E_h1wome8Jc/540x406" alt="" class="responsive-img">
                                        <div class="black-text">
                                            {{ friend.first_name }} {{ friend.last_name }}
                                        </div>
                                    </div>
                                </button>
                            </div>
                        </a>
                    {% endfor %}
                {% else %}
                    <p>No friends yet</p>
                {% endif %}
            </div>

            <div class="column-container-1-item-size-two">
            {% if request.user.username == user.username %}
                <div class="section-title">
                    New post
                </div>
                <div>
                    <form method="POST" class="input-field col ">{% csrf_token %}
                        <label for="new-post"></label>
                        <textarea id="new-post"
                                  class="materialize-textarea"
                                  placeholder="Type your new post"
                                  name="text"
                        ></textarea>
                        <button type="submit" class="right">Post</button>
                    </form>
                </div>
            {% endif %}
                <div class="section-title">
                   Wall
                </div>
                <div class="posts">
                {% if user.post_set.exists %}
                    {% for post in user.post_set.all %}
                        <div class="post">
                            <div class="text">{{ post.text }}</div>
                            <div class="datetime">{{ post.datetime_posted }}</div>
                            <div class="post-author">{{ post.author|capfirst }}</div>
                        </div>
                    {% endfor %}
                {% else %}
                <div>No posts yet!</div>
                {% endif %}
                </div>
            </div>
        </div>
    </div>

</div>

<script src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
        crossorigin="anonymous">
</script>
<script type="text/javascript"
        src="{% static 'social_network_app/js/profile.js' %}">
</script>
<!-- Compiled and minified JavaScript -->


<script>
    const csrfToken = '{{ csrf_token }}';
    const currentUser = '{{request.user.pk}}';
    if (currentUser) {
        addClickListenerToAddFriendButton(currentUser, {{user.pk}}, csrfToken);
    }
</script>

</body>
</html>
```

---

5 -  Add more CSS to style your page

We will add more CSS, To do this:
- Add the below CSS to the bottom of your ```profile.css```file.
```
.post {
    box-shadow: 0px 0px 2px 2px lightgrey;
    border-radius: 15px;
    padding: 20px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.text {
    text-align: left;
    font-size: 18px;
}

.datetime {
    font-size: 14px;
    text-align: right;
    color: lightgrey;
    font-style: italic;
    float: right;
}

.post-author {
    font-size: 14px;
    text-align: left;
    color: lightgrey;
    font-style: italic;
}
```

Now check out your page! Each user is now able to add posts to his or her profile page!
Notice how a user can only post a new post on his or her own page.


<h1>Add a Feed</h1>
--

Let's now create a 'Feed' page. This Feed will allow each user to see all of his/her posts
and friends' posts.

We will follow the same approach as usual:

-> Create a template

-> Create a view, and

-> Create a url route to connect the browser to the view and template

Note that you could do the above steps in any order. I normally prefer 
first to draft the user interface (the UI) that the user will see. This 
means that I normally start by writing the template, but this may vary :)

1 - Create a template for the feed
To do this,
 - ```cd mysite/social_network_app/templates/social_network_app```
 - ```touch feed.html```  # Create the feed.html file
 
 - Open feed.html. Then add the following:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Feed</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>

<nav>
    <div class="nav-wrapper">
        <a href="#" class="brand-logo">The Social Network</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href=""></a></li>
            {% if request.user.username %}
                <li><a href="{% url 'profile' username=request.user.username %}">{{ request.user.first_name }}</a></li>
            {% else %}
                <li><a href="">Guest</a></li>
            {% endif %}
            <li><a href="{% url 'logout' %}"><i class="material-icons">exit_to_app</i></a>
                Logout
            </li>
        </ul>
    </div>
</nav>
<body>
<div class="feed-heading-container">
    <div class="feed-heading-text">
        Feed
    </div>
</div>
<div class="feed-outer-container">
    <div class="feed-inner-container-size-three"></div>
    {% if feed_posts %}
        {% for post in feed_posts %}
            <a href="{% url 'profile' username=post.author.username %}">
            <div class="feed-item-row">
                <div class="feed-item-inner ">
                    <div class="profile-picture-container">
                        <img src="http://source.unsplash.com/E_h1wome8Jc/108x82" alt=""
                             class="circle responsive-img profile-picture-image">
                    </div>
                    <div class="post-author">
                        <div></div>
                        {{ post.author|capfirst }}
                    </div>
                </div>
                <div class="feed-item-inner post-right">
                    <div class="post-detail">
                        <div class="text">{{ post.text }}</div>
                        <div class="datetime">{{ post.datetime_posted }}</div>
                    </div>
                </div>
            </div>
            </a>
        {% endfor %}
    {% else %}
        <div>You and your friends have no posts yet!</div>
    {% endif %}
    <div class="feed-inner-container-size-one"></div>
</div>
</body>
</html>
```

2 - Create a view

- Go to your ```views.py``` file.
- Add the below to the bottom of ```views.py``` (I have added comments with some explanation after the #; feel free to delete these!):

```
@login_required
def feed_view(request):
    if request.method == 'GET':
        user = CustomUser.objects.get(username=request.user.username)  # Get the CustomUser instance of the current user.
        user_posts = Post.objects.filter(author=user)  # Get the user's posts from the database.
        print(user, user_posts)
        friends_posts = Post.objects.filter(author__in=user.friends.all())  # Get the user's friends posts from the database.
        feed_posts = user_posts | friends_posts  # Merge user_posts and friends_posts.
        return render(request, 'social_network_app/feed.html', {'feed_posts': feed_posts})  # Render the template and send the feed posts to the template.
```

---

3 - Add a url route in your ``ùrls.py``
- Go to your ```mysite/social_network_app/urls.py``` file.
- Update your urls to add the new url at the bottom of the file:
```
from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:username>', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-friend/', views.add_friend_view, name='add-friend'),
    path('signup/', views.signup_view, name='signup'),
    path('feed/', views.feed_view, name='feed'),  # The new url
]
```

---
<h3>Check out the Feed at the url that you defined, i.e., /social-network/feed/</h3>
It is great to see the feed! However, let us make it more visually appealing 
with styling.



4 - Style the feed template
To do this:
- In the same way as with our profile template, create a css file for the feed template.
```cd mysite/social_network_app/static/social_network_app/css/```
```touch feed.css```

- Copy and paste the below CSS into ```feed.css```:


```
body {
    background-color: #fff0f005;
}

.feed-heading-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}

.feed-heading-text {
    font-size: 60px;
    display: block;
    margin-top: -40px;
}



.feed-outer-container {
    flex-direction: column;
    text-align: center;
    width: 42%;
    margin: auto;
}

.feed-inner-container-size-one{
    flex: 1
}

.feed-inner-container-size-three {
    flex: 3
}

.feed-item-row {
    display: flex;
    flex-direction: row;
    box-shadow: 0px 2px 6px 0px lightgrey;
    margin-top: 20px;
    margin-bottom: 20px;
    padding-bottom: 20px;
    padding-top: 10px;
    border-radius: 10px;
    background-color: #fff8f8;
    color: black;
}

.feed-item-row:hover {
    background-color: #ee6e6ef2;
    transition: background-color 0.3s;
    color: white;
}


.post-right{
    width: 100%;
}

.post {
    box-shadow: 0px 0px 2px 2px lightgrey;
    border-radius: 15px;
    padding: 28px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.text {
    text-align: left;
    font-size: 18px;
}

.datetime {
    font-size: 14px;
    text-align: right;
    color: lightgrey;
    font-style: italic;
    float: right;
    padding-right: 27px;
}

.post-author {
    font-size: 14px;
    text-align: left;
    font-style: italic;
    padding-left: 20px;
    padding-right: 20px;
}

.post-detail {
    padding-top: 10px;
    padding-bottom: 22px;
    padding-left: 10px;
}

.profile-picture-container{
    padding-left: 10px;
}

.profile-picture-image{
    box-shadow: 0px 1px 0px 3px #7d6c6e38;
}
```


- Connect the CSS file to the template by adding the below line to anywhere between the first `<head> tag and the first `</head>` tag
in your ```feed.html``` template:
```
<link rel="stylesheet" type="text/css" href="{% static 'social_network_app/css/feed.css' %}">
```

- Add the below line immediately above the first `<head>` tag in your ```feed.html``` template:
```
{% load static %}
```

Finally, we'll add links to the feed in the ```profile.html```and ```feed.html``` templates:
To do this:
- In your ```profile.html```, add the following line to the commented position in the block below:

```<li><a href="{% url 'feed' %}">Feed</a></li>```


```
<div class="nav-wrapper">
        <a href="#" class="brand-logo">The Social Network</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href="{% url 'feed' %}">Feed</a></li>
            <li><a href=""></a></li>
            {% if request.user.username %}
            ...
```

In your ```feed.html```, add the same line in the same position.


Congratulations - our basic social network app is taking shape!
Tom to explain Point about duplicating -> DRY


---

Add an individual profile picture and cover photo for every user
---

Currently, all user's profile pictures are fetched from a photo that I took 
that is stored on an online photo site called unsplash.com (I highly recommend unsplash for 
high quality licence free images).

However, we want each user to be able to select images as the user's profile picture and cover photo

To accomplish this, we will store urls to the images in our database. The user may specify these
image urls when they signup.

To do this:
1 - Update your ```signup.html``` template to include the following:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Signup</title>
</head>
<body>
<nav>
    <h1>The Social Network</h1>
</nav>
<form method="POST">
    {% csrf_token %}
    <div>
        <input type="text" name="first_name" placeholder="First name">
    </div>
    <br>
    <div>
        <input type="text" name="last_name" placeholder="Last name">
    </div>
    <br>
    <div>
        <input type="text" name="username" placeholder="Username">
    </div>
    <br>
    <div>
        <input type="password" name="password" placeholder="Password">
    </div>
    <br>
    <div>
        <input type="email" name="email" placeholder="Email">
    </div>
    <br>
    <div>
        <input type="url" name="cover-picture" placeholder="Cover picture url">
    </div>
    <br>
    <div>
        <input type="url" name="profile-picture" placeholder="Profile picture url">
    </div>
    <button type="submit">
        Sign up!
    </button>
</form>

</body>
</html>
```

2 - Update your signup_view in your ```views.py``` to include the following:
```
def signup_view(request):
    if request.method == 'POST':
        default_profile_picture_url = 'https://source.unsplash.com/UHjW9-c_YyM'
        default_cover_photo_url = 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&fit=crop&ixid=eyJhcHBfaWQiOjF9'
        CustomUser.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            cover_picture=request.POST['cover-picture'] or default_cover_photo_url,
            profile_picture=request.POST['profile-picture'] or default_profile_picture_url
        )
        return redirect('login')
    else:
        return render(request, 'social_network_app/signup.html')
```


3 - Update your CustomUser model in your ```models.py```.
To do this:
- Update ```models.py``` to include the following:

```
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
    cover_picture = models.URLField(
        max_length=400,
    )
    profile_picture = models.URLField(
        max_length=400,
    )
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    friends = models.ManyToManyField('self')

    def __str__(self) -> str:
        return str(self.username)
```

4 - Then, as before, makemigrations and then migrate:
- ```cd social_network_app/mysite/manage.py```
- ```python manage.py makemigrations -n added_url_fields```
- ```python migrate```


5 -  Update your templates:
- Replace the html in ```profile.html``` with the following:

```
<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link rel="stylesheet" type="text/css" href="{% static 'social_network_app/css/profile.css' %}">
    <link href="https://fonts.googleapis.com/css?family=Vollkorn+SC&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <meta charset="UTF-8">
    <title>User Profile</title>
</head>

<body>
<nav>
    <div class="nav-wrapper">
        <a href="#" class="brand-logo">The Social Network</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href="{% url 'feed' %}">Feed</a></li>
            <li><a href=""></a></li>
            {% if request.user.username %}
                <li><a href="{% url 'profile' username=request.user.username %}">{{ request.user.first_name }}</a></li>
            {% else %}
                <li><a href="">Guest</a></li>
            {% endif %}
            <li><a href="{% url 'logout' %}"><i class="material-icons">exit_to_app</i></a>
                Logout
            </li>
        </ul>
    </div>
</nav>

<div class="card top-container">
    <div class="card-image waves-effect waves-block waves-light cover-photo-container">
        <img class="cover-photo"
             src="{{ user.cover_picture }}"
             alt="Cover picture image not found"
        >
    </div>
    <div class="profile-picture-container card-content">
           <div class="">
<img src="{{ user.profile_picture }}"
     height="150px"
     width="150px"
     alt=""
     class="circle responsive-img profile-picture-container">
<!-- notice the "circle" class -->
           <div class="profile-name grey-text ">
               {{ user.first_name }} {{ user.last_name }}
           </div>
               <div class="personal-details grey-text text-darken-5">
                   <p><i>{{ user.email }}</i></p>
                   <p><i>{{ user.username }}</i></p>
               </div>
               <div class="right add-friend-container">
                    {% if request.user.pk != user.pk %}
                        {% if request.user in user.friends.all %}
                            <button type="button" class="btn waves-effect waves-light pink">
                                Is a friend <i class="material-icons">person</i>
                            </button>
                        {% else %}
                            <button type="button" class="btn waves-effect waves-light blue" id="add-friend-button">
                                <i class="material-icons">person_add</i>
                            Add friend
                            </button>
                        {% endif %}
                    {% endif %}
                </div>

            <div>

            </div>
        </div>
    </div>
    <div class="section-container">

    </div>
    <div class="section-container">
        <div class="column-container-1">
            <div class="column-container-1-item-size-one">
                <div class="section-title">
                    Interests
                    <div class="section-text">
                        <ul>
                            <li>Rock sailing </li>
                            <li>Water hiking</li>
                            <li>Pit jumping</li>
                            <li>Forest rafting</li>
                            <li>Loud Shouting</li>
                        </ul>
                    </div>
                </div>
                <div class="section-title">Friends
                    <i class="material-icons friends-icon">group</i>
                </div>
                {% if user.friends.all %}
                    {% for friend in user.friends.all %}
                        <a href="{% url 'profile' username=friend.username %}">
                            <div class="row valign-wrapper current-friend-container">
                                <button type="submit">
                                    <div class="current-friend-card">
                                        <img src="{{ friend.profile_picture }}"
                                             alt=""
                                             height="150px"
                                             width="150px"
                                             class="responsive-img">
                                        <div class="black-text">
                                            {{ friend.first_name }} {{ friend.last_name }}
                                        </div>
                                    </div>
                                </button>
                            </div>
                        </a>
                    {% endfor %}
                {% else %}
                    <p>No friends yet</p>
                {% endif %}
            </div>

            <div class="column-container-1-item-size-two">
            {% if request.user.username == user.username %}
                <div class="section-title">
                    New post
                </div>
                <div>
                    <form method="POST" class="input-field col ">{% csrf_token %}
                        <label for="new-post"></label>
                        <textarea id="new-post"
                                  class="materialize-textarea"
                                  placeholder="Type your new post"
                                  name="text"
                        ></textarea>
                        <button type="submit" class="right">Post</button>
                    </form>
                </div>
            {% endif %}
                <div class="section-title">
                   Wall
                </div>
                <div class="posts">
                {% if user.post_set.exists %}
                    {% for post in user.post_set.all %}
                        <div class="post">
                            <div class="text">{{ post.text }}</div>
                            <div class="datetime">{{ post.datetime_posted }}</div>
                            <div class="post-author">{{ post.author|capfirst }}</div>
                        </div>
                    {% endfor %}
                {% else %}
                <div>No posts yet!</div>
                {% endif %}
                </div>
            </div>
        </div>
    </div>

</div>

<script src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
        crossorigin="anonymous">
</script>
<script type="text/javascript"
        src="{% static 'social_network_app/js/profile.js' %}">
</script>
<!-- Compiled and minified JavaScript -->


<script>
    const csrfToken = '{{ csrf_token }}';
    const currentUser = '{{request.user.pk}}';
    if (currentUser) {
        addClickListenerToAddFriendButton(currentUser, {{user.pk}}, csrfToken);
    }
</script>

</body>
</html>
```

6 - Then update your ```feed.html``` template
Replace the `feed.html with the below:
```
<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <title>Feed</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="{% static 'social_network_app/css/feed.css' %}">
</head>

<nav>
    <div class="nav-wrapper">
        <a href="#" class="brand-logo">The Social Network</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href="{% url 'feed' %}">Feed</a></li>
            <li><a href=""></a></li>
            {% if request.user.username %}
                <li><a href="{% url 'profile' username=request.user.username %}">{{ request.user.first_name }}</a></li>
            {% else %}
                <li><a href="">Guest</a></li>
            {% endif %}
            <li><a href="{% url 'logout' %}"><i class="material-icons">exit_to_app</i></a>
                Logout
            </li>
        </ul>
    </div>
</nav>
<body>
<div class="feed-heading-container">
    <div class="feed-heading-text">
        Feed
    </div>
</div>
<div class="feed-outer-container">
    <div class="feed-inner-container-size-three"></div>
    {% if feed_posts %}
        {% for post in feed_posts %}
            <a href="{% url 'profile' username=post.author.username %}">
            <div class="feed-item-row">
                <div class="feed-item-inner ">
                    <div class="profile-picture-container">
                        <img src="{{ post.author.profile_picture }}"
                             width="200px"
                             height="200px"
                             alt=""
                             class="circle responsive-img profile-picture-image">
                    </div>
                    <div class="post-author">
                        <div></div>
                        {{ post.author|capfirst }}
                    </div>
                </div>
                <div class="feed-item-inner post-right">
                    <div class="post-detail">
                        <div class="text">{{ post.text }}</div>
                        <div class="datetime">{{ post.datetime_posted }}</div>
                    </div>
                </div>
            </div>
            </a>
        {% endfor %}
    {% else %}
        <div>You and your friends have no posts yet!</div>
    {% endif %}
    <div class="feed-inner-container-size-one"></div>
</div>
</body>
</html>
```

#Congratulations! 
Users are now able to specify their own cover picture and profile 
picture when they signup!



Next steps:
- Add comments to your posts
- Add a search bar for user's to find their friends and potential friends
- Add likes/dislikes/loves/joy/melancholy/wistful longing/sense of triumphant 
overcoming/happiness buttons to allow users to indicate their emotional reactions 
to posts and comments
- Add the ability for users to upload their own images and to change their 
profile pciture and cover picture 
