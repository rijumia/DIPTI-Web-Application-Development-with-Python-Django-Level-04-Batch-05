\### Riju Mia

answer(Theory with example) all question

\## 🔹 \*\*Django Fundamentals\*\*

\### \*\*1. What is Django?\*\*

\*\*Theory:\*\*

Django is a high-level, open-source Python web framework that encourages rapid development and clean, pragmatic design. It follows the \*\*MVT (Model-View-Template)\*\* architectural pattern and handles much of the complexity of web development, allowing developers to focus on building applications without reinventing the wheel.

\*\*Example:\*\*

You can create a blog, e-commerce site, or API backend using Django in a structured and secure way.

\---

\### \*\*2. What are the main features of Django?\*\*

\*\*Theory:\*\*

Django provides several powerful features:

\- \*\*ORM (Object-Relational Mapper):\*\* Interact with databases using Python instead of SQL.

\- \*\*Admin Interface:\*\* Auto-generated admin panel for managing data.

\- \*\*Authentication:\*\* Built-in user login, logout, permissions, and groups.

\- \*\*URL Routing:\*\* Clean and readable URL design.

\- \*\*Templates:\*\* HTML templates with logic and inheritance.

\- \*\*Security:\*\* Protection against CSRF, XSS, SQL injection.

\- \*\*Scalability:\*\* Used by high-traffic sites like Instagram and Pinterest.

\*\*Example:\*\*

Using Django's ORM, you can write:

\`\`\`python

posts = Post.objects.all()

\`\`\`

instead of:

\`\`\`sql

SELECT \* FROM blog\_post;

\`\`\`

\---

\### \*\*3. What is the default database supported by Django?\*\*

\*\*Theory:\*\*

Django’s default database is \*\*SQLite3\*\*, a lightweight, file-based database that requires no separate server setup.

\*\*Example:\*\*

In \`settings.py\`:

\`\`\`python

DATABASES = {

'default': {

'ENGINE': 'django.db.backends.sqlite3',

'NAME': BASE\_DIR / 'db.sqlite3',

}

}

\`\`\`

\---

\### \*\*4. How do you create a Django project?\*\*

\*\*Theory:\*\*

Use the \`django-admin\` command-line utility to create a project.

\*\*Example:\*\*

\`\`\`bash

django-admin startproject myproject

cd myproject

python manage.py runserver

\`\`\`

This creates the base project structure including \`manage.py\`, \`settings.py\`, \`urls.py\`, etc.

\---

\### \*\*5. What is the use of manage.py in Django?\*\*

\*\*Theory:\*\*

\`manage.py\` is a command-line utility that lets you interact with your Django project. It’s an alternative to \`django-admin\` with project-specific settings pre-loaded.

\*\*Common Uses:\*\*

\`\`\`bash

python manage.py runserver # Start dev server

python manage.py makemigrations # Create migration files

python manage.py migrate # Apply migrations

python manage.py createsuperuser # Create admin user

\`\`\`

\---

\### \*\*6. How do you start a new app in a Django project?\*\*

\*\*Theory:\*\*

An app is a modular component of a Django project (e.g., blog, users, products).

\*\*Example:\*\*

\`\`\`bash

python manage.py startapp blog

\`\`\`

Then add \`'blog'\` to \`INSTALLED\_APPS\` in \`settings.py\`.

\---

\### \*\*7. What is the difference between a project and an app in Django?\*\*

\*\*Theory:\*\*

\- \*\*Project:\*\* The entire web application (e.g., a website).

\- \*\*App:\*\* A module within the project that handles a specific function (e.g., blog, authentication).

\*\*Example:\*\*

A project \`mywebsite\` might contain apps: \`blog\`, \`shop\`, \`users\`.

\---

\### \*\*8. What is the role of settings.py in a Django project?\*\*

\*\*Theory:\*\*

\`settings.py\` contains all configuration for the Django project: database settings, installed apps, middleware, static files, security settings, etc.

\*\*Example:\*\*

\`\`\`python

INSTALLED\_APPS = \[

'django.contrib.admin',

'django.contrib.auth',

'blog.apps.BlogConfig',

\]

ALLOWED\_HOSTS = \['localhost', '127.0.0.1'\]

\`\`\`

\---

\### \*\*9. How do you set up a database connection in Django?\*\*

\*\*Theory:\*\*

Configure the \`DATABASES\` dictionary in \`settings.py\`.

\*\*Example (PostgreSQL):\*\*

\`\`\`python

DATABASES = {

'default': {

'ENGINE': 'django.db.backends.postgresql',

'NAME': 'mydb',

'USER': 'myuser',

'PASSWORD': 'mypassword',

'HOST': 'localhost',

'PORT': '5432',

}

}

\`\`\`

\---

\## 🔹 \*\*Django Models & ORM\*\*

\### \*\*10. What is a Django model? / What is a Django model in the context of web development?\*\*

\*\*Theory:\*\*

A model is a Python class that represents a database table. It defines the structure of data (fields, relationships) and is used by Django’s ORM.

\*\*Example:\*\*

\`\`\`python

from django.db import models

class Post(models.Model):

title = models.CharField(max\_length=100)

content = models.TextField()

created\_at = models.DateTimeField(auto\_now\_add=True)

\`\`\`

This creates a \`blog\_post\` table in the database.

\---

\### \*\*11. How do you define a model in Django?\*\*

\*\*Theory:\*\*

Create a class in \`models.py\` that inherits from \`models.Model\` and define fields as class variables.

\*\*Example:\*\*

\`\`\`python

class Author(models.Model):

name = models.CharField(max\_length=100)

email = models.EmailField(unique=True)

\`\`\`

\---

\### \*\*12. What is the purpose of the models.py file in a Django app?\*\*

\*\*Theory:\*\*

\`models.py\` contains all model definitions for the app. Django uses these to create database tables via migrations.

\---

\### \*\*13. What is Django ORM? What database operations can be performed using Django's ORM, give example?\*\*

\*\*Theory:\*\*

Django ORM (Object-Relational Mapper) allows you to interact with the database using Python code instead of SQL.

\*\*Operations:\*\*

\- \*\*Create:\*\* \`Post.objects.create(title="Hello")\`

\- \*\*Read:\*\* \`Post.objects.all()\`, \`Post.objects.get(id=1)\`

\- \*\*Update:\*\* \`post.title = "New"; post.save()\`

\- \*\*Delete:\*\* \`post.delete()\`

\*\*Example:\*\*

\`\`\`python

\# Create

post = Post(title="My Post", content="Hello")

post.save()

\# Read

posts = Post.objects.filter(title\_\_icontains="My")

\# Update

post = Post.objects.get(id=1)

post.title = "Updated"

post.save()

\# Delete

post.delete()

\`\`\`

\---

\### \*\*14. What is the significance of the id field in Django models? / What is the default primary key field in Django models?\*\*

\*\*Theory:\*\*

Django automatically adds an \`id\` field as the primary key unless specified otherwise. It’s an auto-incrementing integer.

\*\*Example:\*\*

\`\`\`python

class Post(models.Model):

\# id = models.AutoField(primary\_key=True) <-- added automatically

title = models.CharField(max\_length=100)

\`\`\`

\---

\### \*\*15. How do you define a field as a primary key in Django?\*\*

\*\*Theory:\*\*

Use \`primary\_key=True\`.

\*\*Example:\*\*

\`\`\`python

class Employee(models.Model):

emp\_id = models.CharField(max\_length=10, primary\_key=True)

name = models.CharField(max\_length=100)

\`\`\`

\---

\### \*\*16. Name some commonly used field types in Django models.\*\*

\*\*Theory:\*\*

\- \`CharField\` – for short text (e.g., name)

\- \`TextField\` – for long text

\- \`IntegerField\`, \`FloatField\`

\- \`BooleanField\`

\- \`DateTimeField\`, \`DateField\`

\- \`EmailField\`, \`URLField\`

\- \`ForeignKey\`, \`ManyToManyField\`, \`OneToOneField\`

\- \`FileField\`, \`ImageField\`

\---

\### \*\*17. What is the purpose of CharField and TextField in Django models?\*\*

\*\*Theory:\*\*

\- \`CharField\`: For small strings (requires \`max\_length\`)

\- \`TextField\`: For large blocks of text (no \`max\_length\` required)

\*\*Example:\*\*

\`\`\`python

title = models.CharField(max\_length=200) # For titles

body = models.TextField() # For article content

\`\`\`

\---

\### \*\*18. How does ForeignKey work in Django models?\*\*

\*\*Theory:\*\*

\`ForeignKey\` creates a one-to-many relationship. One record in a model can be linked to multiple records in another.

\*\*Example:\*\*

\`\`\`python

class Author(models.Model):

name = models.CharField(max\_length=100)

class Post(models.Model):

author = models.ForeignKey(Author, on\_delete=models.CASCADE)

title = models.CharField(max\_length=100)

\`\`\`

One author can have many posts.

\---

\### \*\*19. What is a ManyToManyField in Django, and when should you use it?\*\*

\*\*Theory:\*\*

\`ManyToManyField\` creates a many-to-many relationship (e.g., a student can take many courses, a course can have many students).

\*\*Example:\*\*

\`\`\`python

class Student(models.Model):

name = models.CharField(max\_length=100)

class Course(models.Model):

title = models.CharField(max\_length=100)

students = models.ManyToManyField(Student)

\`\`\`

\---

\### \*\*20. What is the difference between DateField and DateTimeField?\*\*

\*\*Theory:\*\*

\- \`DateField\`: Stores only date (YYYY-MM-DD)

\- \`DateTimeField\`: Stores date and time (YYYY-MM-DD HH:MM:SS)

\*\*Example:\*\*

\`\`\`python

birth\_date = models.DateField() # 1990-01-01

created\_at = models.DateTimeField() # 2025-04-05 10:30:00

\`\`\`

\---

\### \*\*21. What is the purpose of the Meta class in a Django model?\*\*

\*\*Theory:\*\*

The \`Meta\` class inside a model defines metadata like \`verbose\_name\`, \`ordering\`, \`db\_table\`, etc.

\*\*Example:\*\*

\`\`\`python

class Post(models.Model):

title = models.CharField(max\_length=100)

class Meta:

verbose\_name\_plural = "Posts"

ordering = \['-created\_at'\]

db\_table = 'blog\_posts'

\`\`\`

\---

\### \*\*22. How can you make a model field unique?\*\*

\*\*Theory:\*\*

Use \`unique=True\`.

\*\*Example:\*\*

\`\`\`python

email = models.EmailField(unique=True)

\`\`\`

\---

\### \*\*23. What is the use of db\_index=True in a model field?\*\*

\*\*Theory:\*\*

\`db\_index=True\` creates a database index on the field for faster queries.

\*\*Example:\*\*

\`\`\`python

username = models.CharField(max\_length=100, db\_index=True)

\`\`\`

\---

\### \*\*24. How can you order querysets by default for a model?\*\*

\*\*Theory:\*\*

Use \`ordering\` in the \`Meta\` class.

\*\*Example:\*\*

\`\`\`python

class Meta:

ordering = \['title'\] # Ascending

\# or \['-title'\] for descending

\`\`\`

\---

\### \*\*25. What is the difference between OneToOneField, ForeignKey, and ManyToManyField?\*\*

\*\*Theory:\*\*

\- \`OneToOneField\`: One record linked to exactly one other (e.g., User → Profile)

\- \`ForeignKey\`: One-to-many (e.g., Author → Posts)

\- \`ManyToManyField\`: Many-to-many (e.g., Students ↔ Courses)

\*\*Example:\*\*

\`\`\`python

class Profile(models.Model):

user = models.OneToOneField(User, on\_delete=models.CASCADE)

class Post(models.Model):

author = models.ForeignKey(Author, on\_delete=models.CASCADE)

class Course(models.Model):

students = models.ManyToManyField(Student)

\`\`\`

\---

\### \*\*26. How do you set up a self-referential ForeignKey in a model?\*\*

\*\*Theory:\*\*

A model references itself (e.g., employee and manager).

\*\*Example:\*\*

\`\`\`python

class Employee(models.Model):

name = models.CharField(max\_length=100)

manager = models.ForeignKey('self', on\_delete=models.SET\_NULL, null=True)

\`\`\`

\---

\### \*\*27. How do you define a related name for a ForeignKey field?\*\*

\*\*Theory:\*\*

\`related\_name\` allows reverse lookup from the related model.

\*\*Example:\*\*

\`\`\`python

class Author(models.Model):

name = models.CharField(max\_length=100)

class Post(models.Model):

author = models.ForeignKey(Author, on\_delete=models.CASCADE, related\_name='posts')

\`\`\`

Now you can do: \`author.posts.all()\`

\---

\### \*\*28. What is on\_delete in a ForeignKey, and what options are available?\*\*

\*\*Theory:\*\*

Specifies what happens when the referenced object is deleted.

\*\*Options:\*\*

\- \`models.CASCADE\` – Delete child objects

\- \`models.SET\_NULL\` – Set to NULL (requires \`null=True\`)

\- \`models.PROTECT\` – Prevent deletion

\- \`models.SET\_DEFAULT\` – Set to default

\- \`models.DO\_NOTHING\` – Do nothing

\*\*Example:\*\*

\`\`\`python

author = models.ForeignKey(Author, on\_delete=models.SET\_NULL, null=True)

\`\`\`

\---

\### \*\*29. How do you retrieve related objects for a ManyToManyField?\*\*

\*\*Theory:\*\*

Use the field name directly.

\*\*Example:\*\*

\`\`\`python

course = Course.objects.get(id=1)

students = course.students.all() # All students in course

\`\`\`

\---

\### \*\*30. What is the purpose of the auto\_now\_add option in a Django DateTimeField?\*\*

\*\*Theory:\*\*

\`auto\_now\_add=True\` sets the field to the current time when the object is \*\*first created\*\*. It’s immutable.

\*\*Example:\*\*

\`\`\`python

created\_at = models.DateTimeField(auto\_now\_add=True)

\`\`\`

\> Use \`auto\_now=True\` for fields that update on every save (e.g., \`updated\_at\`).

\---

\### \*\*31. How do you create a new database record (object) using Django ORM? / How do you create a new record in the database using Django ORM?\*\*

\*\*Theory:\*\*

Use \`create()\` or instantiate and \`save()\`.

\*\*Example:\*\*

\`\`\`python

\# Method 1: create()

Post.objects.create(title="New Post", content="Hello")

\# Method 2: save()

post = Post(title="Another", content="World")

post.save()

\`\`\`

\---

\### \*\*32. How do you retrieve all records from a model?\*\*

\*\*Theory:\*\*

Use \`.all()\`.

\*\*Example:\*\*

\`\`\`python

posts = Post.objects.all()

\`\`\`

\---

\### \*\*33. How do you filter objects in a queryset?\*\*

\*\*Theory:\*\*

Use \`.filter()\`.

\*\*Example:\*\*

\`\`\`python

posts = Post.objects.filter(title\_\_icontains="django")

\`\`\`

\---

\### \*\*34. How do you retrieve the first or last object from a queryset?\*\*

\*\*Theory:\*\*

Use \`.first()\` or \`.last()\`.

\*\*Example:\*\*

\`\`\`python

first\_post = Post.objects.all().first()

last\_post = Post.objects.all().last()

\`\`\`

\---

\### \*\*35. What is the difference between all() and values() in a queryset?\*\*

\*\*Theory:\*\*

\- \`all()\` returns model instances.

\- \`values()\` returns dictionaries.

\*\*Example:\*\*

\`\`\`python

Post.objects.all() # \[, ...\]

Post.objects.values() # \[{'id': 1, 'title': 'Hello'}, ...\]

\`\`\`

\---

\### \*\*36. How do you perform aggregation in a Django queryset?\*\*

\*\*Theory:\*\*

Use \`aggregate()\` with functions like \`Count\`, \`Sum\`, \`Avg\`.

\*\*Example:\*\*

\`\`\`python

from django.db.models import Count

count = Post.objects.aggregate(Count('id'))

\# {'id\_\_count': 5}

\`\`\`

\---

\### \*\*37. How do you delete a record in Django ORM? / How do you delete a record in Django models?\*\*

\*\*Theory:\*\*

Call \`.delete()\` on an object or queryset.

\*\*Example:\*\*

\`\`\`python

post = Post.objects.get(id=1)

post.delete()

\`\`\`

\---

\### \*\*38. How do you perform a bulk delete operation on multiple records in Django models? / How can you delete multiple records in Django ORM?\*\*

\*\*Theory:\*\*

Call \`.delete()\` on a filtered queryset.

\*\*Example:\*\*

\`\`\`python

Post.objects.filter(created\_at\_\_year=2020).delete()

\`\`\`

\---

\### \*\*39. What is the purpose of the choices attribute in a model field?\*\*

\*\*Theory:\*\*

Limits field values to a predefined list.

\*\*Example:\*\*

\`\`\`python

STATUS\_CHOICES = \[('D', 'Draft'), ('P', 'Published')\]

status = models.CharField(max\_length=1, choices=STATUS\_CHOICES)

\`\`\`

\---

\### \*\*40. What is the difference between blank=True and null=True in Django models?\*\*

\*\*Theory:\*\*

\- \`blank=True\`: Field can be empty in forms.

\- \`null=True\`: Field can be NULL in the database.

\*\*Example:\*\*

\`\`\`python

bio = models.TextField(blank=True, null=True)

\`\`\`

\- \`blank=True\` → form validation allows empty

\- \`null=True\` → database allows NULL

\---

\### \*\*41. How do you handle image uploads in a Django model?\*\*

\*\*Theory:\*\*

Use \`ImageField\`. Requires \`Pillow\` library.

\*\*Example:\*\*

\`\`\`python

from django.db import models

class Profile(models.Model):

avatar = models.ImageField(upload\_to='avatars/')

\`\`\`

Add to \`settings.py\`:

\`\`\`python

MEDIA\_URL = '/media/'

MEDIA\_ROOT = BASE\_DIR / 'media'

\`\`\`

\---

\### \*\*42. What is the use of verbose\_name and verbose\_name\_plural in Django models?\*\*

\*\*Theory:\*\*

Customizes how the model appears in the admin panel.

\*\*Example:\*\*

\`\`\`python

class Meta:

verbose\_name = "Blog Post"

verbose\_name\_plural = "Blog Posts"

\`\`\`

\---

\## 🔹 \*\*Migrations\*\*

\### \*\*43. What are makemigrations and migrate commands in Django?\*\*

\*\*Theory:\*\*

\- \`makemigrations\`: Creates migration files based on model changes.

\- \`migrate\`: Applies migrations to the database.

\*\*Example:\*\*

\`\`\`bash

python manage.py makemigrations

python manage.py migrate

\`\`\`

\---

\### \*\*44. What command is used to apply changes to the database after modifying models?\*\*

\*\*Answer:\*\* \`python manage.py migrate\`

\---

\### \*\*45. Which Django command is used to generate the necessary database schema based on the model?\*\*

\*\*Answer:\*\* \`makemigrations\` and \`migrate\`

\---

\### \*\*46. How can you perform database migrations in Django?\*\*

\*\*Theory:\*\*

1\. Make model changes.

2\. Run \`makemigrations\`.

3\. Run \`migrate\`.

\---

\### \*\*47. How do you add a new field to an existing model?\*\*

\*\*Example:\*\*

\`\`\`python

\# In models.py

class Post(models.Model):

published = models.BooleanField(default=False) # new field

\`\`\`

Then:

\`\`\`bash

python manage.py makemigrations

python manage.py migrate

\`\`\`

\---

\### \*\*48. What is a migration file in Django?\*\*

\*\*Theory:\*\*

A Python file in \`migrations/\` that records changes to models so Django can update the database schema.

\---

\### \*\*49. How do you rename a field in a Django model?\*\*

\*\*Theory:\*\*

Use \`makemigrations\` after renaming. Django detects the change.

\*\*Example:\*\*

\`\`\`python

\# old: title = models.CharField(...)

\# new: headline = models.CharField(...)

\`\`\`

Run:

\`\`\`bash

python manage.py makemigrations

\`\`\`

\---

\### \*\*50. What happens if you delete a model without applying migrations?\*\*

\*\*Answer:\*\*

The database table remains. You must run \`makemigrations\` and \`migrate\` to actually remove it.

\---

\### \*\*51. How do you define a custom manager for a model?\*\*

\*\*Theory:\*\*

Create a custom \`Manager\` class.

\*\*Example:\*\*

\`\`\`python

class PublishedManager(models.Manager):

def get\_queryset(self):

return super().get\_queryset().filter(status='P')

class Post(models.Model):

status = models.CharField(max\_length=1)

objects = models.Manager()

published = PublishedManager()

\`\`\`

\---

\### \*\*52. What is the purpose of the default argument in a model field?\*\*

\*\*Theory:\*\*

Sets a default value if none is provided.

\*\*Example:\*\*

\`\`\`python

status = models.CharField(max\_length=1, default='D')

\`\`\`

\---

\### \*\*53. How do you set a field to allow null values in the database?\*\*

\*\*Answer:\*\* \`null=True\`

\---

\### \*\*54. How do you set a field to be optional in forms but not null in the database?\*\*

\*\*Answer:\*\* Use \`blank=True, null=False\`, and set a \`default\`.

\---

\### \*\*55. How do you set a default value for a field in Django models?\*\*

\*\*Answer:\*\* \`default='value'\` or \`default=callable\`

\---

\## 🔹 \*\*Views & URLs\*\*

\### \*\*56. What is a view in Django?\*\*

\*\*Theory:\*\*

A view is a Python function or class that receives a web request and returns a response.

\*\*Example (FBV):\*\*

\`\`\`python

def home(request):

return HttpResponse("Hello")

\`\`\`

\---

\### \*\*57. How do you map a view to a URL in Django?\*\*

\*\*Theory:\*\*

Use \`path()\` in \`urls.py\`.

\*\*Example:\*\*

\`\`\`python

\# urls.py

from django.urls import path

from . import views

urlpatterns = \[

path('', views.home, name='home'),

\]

\`\`\`

\---

\### \*\*58. What is the difference between Function-Based Views (FBV) and Class-Based Views (CBV) in Django?\*\*

\*\*Theory:\*\*

\- \*\*FBV:\*\* Functions handle requests.

\- \*\*CBV:\*\* Classes (e.g., \`TemplateView\`, \`ListView\`) with methods like \`get()\`, \`post()\`.

\*\*Example (CBV):\*\*

\`\`\`python

from django.views.generic import ListView

class PostListView(ListView):

model = Post

\`\`\`

\---

\### \*\*59. What is the purpose of the urlpatterns list in Django?\*\*

\*\*Answer:\*\* It maps URLs to views.

\---

\### \*\*60. How do you pass parameters in a URL in Django?\*\*

\*\*Example:\*\*

\`\`\`python

path('post//', views.post\_detail, name='post\_detail')

\`\`\`

In view:

\`\`\`python

def post\_detail(request, id):

post = Post.objects.get(id=id)

\`\`\`

\---

\### \*\*61. What is the purpose of the 'reverse()' function in Django with respect to URLs?\*\*

\*\*Theory:\*\*

\`reverse()\` returns the URL for a given view name.

\*\*Example:\*\*

\`\`\`python

from django.urls import reverse

url = reverse('post\_detail', args=\[1\])

\# Returns: '/post/1/'

\`\`\`

Used in redirects:

\`\`\`python

return redirect(reverse('home'))

\`\`\`

\---

\### \*\*62. What is the difference between path() and re\_path() functions in Django URL patterns?\*\*

\*\*Theory:\*\*

\- \`path()\`: Uses simple syntax (e.g., \`\`)

\- \`re\_path()\`: Uses regular expressions

\*\*Example:\*\*

\`\`\`python

re\_path(r'^post/(?P\[0-9\]+)/$', views.post\_detail)

\`\`\`

\---

\### \*\*63. What is the purpose of a URL pattern in Django?\*\*

\*\*Answer:\*\* To map URLs to views.

\---

\### \*\*64. How is a URL pattern defined in Django's 'urls.py' file?\*\*

\*\*Answer:\*\* Using \`path()\` or \`re\_path()\` in \`urlpatterns\` list.

\---

\## 🔹 \*\*Templates\*\*

\### \*\*65. What is the role of templates in Django?\*\*

\*\*Answer:\*\* Templates define the HTML structure with dynamic content.

\---

\### \*\*66. How do you render a template in a Django view?\*\*

\*\*Example:\*\*

\`\`\`python

from django.shortcuts import render

def home(request):

return render(request, 'home.html', {'name': 'John'})

\`\`\`

\---

\### \*\*67. What is the syntax for using a variable in a Django template?\*\*

\*\*Answer:\*\* \`{{ variable }}\`

\*\*Example:\*\*

\`\`\`html

Hello, {{ name }}!
==================

\`\`\`

\---

\### \*\*68. How can you include one template into another?\*\*

\*\*Answer:\*\* \`{% include 'header.html' %}\`

\---

\### \*\*69. What is the use of {% block %} and {% endblock %} in templates? / What is the purpose of the {% block %} tag in Django templates?\*\*

\*\*Theory:\*\*

For template inheritance.

\*\*Example:\*\*

\`\`\`html

{% block content %}{% endblock %}

{% extends "base.html" %}

{% block content %}

This is content.

{% endblock %}

\`\`\`

\---

\### \*\*70. How do you use a for loop in Django templates?\*\*

\*\*Example:\*\*

\`\`\`html

{% for post in posts %}

{{ post.title }}

{% endfor %}

\`\`\`

\---

\### \*\*71. What is template inheritance in Django?\*\*

\*\*Answer:\*\* A way to define a base template and extend it in child templates.

\---

\### \*\*72. Which template tag is used to perform if-else logic in Django templates?\*\*

\*\*Answer:\*\* \`{% if %}\`, \`{% elif %}\`, \`{% else %}\`

\*\*Example:\*\*

\`\`\`html

{% if user.is\_authenticated %}

Welcome!

{% endif %}

\`\`\`

\---

\### \*\*73. How can conditional logic be used to display "Yes" or "No" in a Django template?\*\*

\*\*Answer:\*\* Use the \`yesno\` filter.

\*\*Example:\*\*

\`\`\`html

{{ user.is\_active|yesno:"Yes,No" }}

\`\`\`

\---

\### \*\*74. What does the 'yesno' filter do in Django templates?\*\*

\*\*Answer:\*\* Maps True/False to custom strings.

\*\*Example:\*\*

\`\`\`html

{{ True|yesno:"Yes,No,N/A" }}

\`\`\`

\---

\### \*\*75. What does the 'date' filter do in Django templates? / What does the ‘date’ filter do in Django templates?\*\*

\*\*Answer:\*\* Formats a date.

\*\*Example:\*\*

\`\`\`html

{{ post.created\_at|date:"F d, Y" }}

\`\`\`

\---

\### \*\*76. What is the purpose of the 'length' filter in Django templates?\*\*

\*\*Answer:\*\* Returns the length of a list or string.

\*\*Example:\*\*

\`\`\`html

{{ posts|length }}

\`\`\`

\---

\### \*\*77. Which template tag is used for escaping HTML content in Django templates?\*\*

\*\*Answer:\*\* \`|escape\` or \`{% autoescape %}\`

\*\*Example:\*\*

\`\`\`html

{{ content|escape }}

\`\`\`

\---

\## 🔹 \*\*Forms\*\*

\### \*\*78. What is a Django form and what is its purpose?\*\*

\*\*Theory:\*\*

A form handles user input (e.g., login, registration).

\---

\### \*\*79. How do you define a form class in Django?\*\*

\*\*Example:\*\*

\`\`\`python

from django import forms

class ContactForm(forms.Form):

name = forms.CharField()

email = forms.EmailField()

\`\`\`

\---

\### \*\*80. What is the difference between ModelForm and forms.Form?\*\*

\*\*Theory:\*\*

\- \`forms.Form\`: General form.

\- \`ModelForm\`: Tied to a model, auto-generates fields.

\*\*Example:\*\*

\`\`\`python

class PostForm(forms.ModelForm):

class Meta:

model = Post

fields = \['title', 'content'\]

\`\`\`

\---

\### \*\*81. How is a Django form submitted in a template?\*\*

\*\*Example:\*\*

\`\`\`html

{% csrf\_token %}

{{ form.as\_p }}

Submit

\`\`\`

\---

\### \*\*82. What method is used to handle submitted data by form in a Django view?\*\*

\*\*Answer:\*\* Check \`request.method == 'POST'\`

\*\*Example:\*\*

\`\`\`python

if request.method == 'POST':

form = ContactForm(request.POST)

if form.is\_valid():

\# Process data

\`\`\`

\---

\### \*\*83. How do you access form data submitted through POST method in a Django view?\*\*

\*\*Answer:\*\* \`request.POST\`

\*\*Example:\*\*

\`\`\`python

name = request.POST.get('name')

\`\`\`

\---

\### \*\*84. How can you handle form submissions in Django views?\*\*

\*\*Answer:\*\* As shown in #82.

\---

\### \*\*85. What is the purpose of the save() function in Django? / What is the purpose and use of the save() function in Django?\*\*

\*\*Theory:\*\*

Saves the model instance to the database.

\*\*Example:\*\*

\`\`\`python

post = Post(title="Test")

post.save() # Now has an ID

\`\`\`

\---

\## 🔹 \*\*Authentication & Admin\*\*

\### \*\*86. What is the role of the 'is\_authenticated' attribute in Django user authentication?\*\*

\*\*Theory:\*\*

\`user.is\_authenticated\` returns \`True\` if the user is logged in.

\*\*Example:\*\*

\`\`\`python

if request.user.is\_authenticated:

\# Show profile

\`\`\`

\---

\### \*\*87. How does Django’s authentication system work?\*\*

\*\*Theory:\*\*

Provides login, logout, password reset, sessions, and permissions via \`django.contrib.auth\`.

\---

\### \*\*88. What is Django Admin, how is it used? / Explain the purpose of the django admin site?\*\*

\*\*Theory:\*\*

Auto-generated admin interface to manage models.

\*\*Register model:\*\*

\`\`\`python

\# admin.py

from django.contrib import admin

from .models import Post

admin.site.register(Post)

\`\`\`

\---

\### \*\*89. How do you register a model with the Django admin site?\*\*

\*\*Answer:\*\* As above.

\---

\### \*\*90. What is the command to create a superuser in Django?\*\*

\*\*Answer:\*\*

\`\`\`bash

python manage.py createsuperuser

\`\`\`

\---

\### \*\*91. How can you customize the Django admin interface for a model?\*\*

\*\*Example:\*\*

\`\`\`python

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):

list\_display = ('title', 'author')

\`\`\`

\---

\### \*\*92. What is the purpose of the admin.py file in a Django app?\*\*

\*\*Answer:\*\* To register and customize models in the admin site.

\---

\### \*\*93. How do you filter data in the Django admin interface?\*\*

\*\*Answer:\*\* Use \`list\_filter\` in \`ModelAdmin\`.

\`\`\`python

list\_filter = ('created\_at',)

\`\`\`

\---

\### \*\*94. What is the default User model in Django?\*\*

\*\*Answer:\*\* \`django.contrib.auth.models.User\`

\---

\### \*\*95. How can you create a custom user model in Django?\*\*

\*\*Answer:\*\* Define a model with \`AbstractUser\` or \`AbstractBaseUser\`.

\---

\### \*\*96. What is CSRF and how is it handled in Django?\*\*

\*\*Answer:\*\* Cross-Site Request Forgery. Django uses \`{% csrf\_token %}\` in forms.

\---

\### \*\*97. What is the purpose of LOGIN\_URL and LOGIN\_REDIRECT\_URL?\*\*

\*\*Answer:\*\*

\- \`LOGIN\_URL\`: Where users are redirected to log in.

\- \`LOGIN\_REDIRECT\_URL\`: Where users go after login.

In \`settings.py\`:

\`\`\`python

LOGIN\_URL = 'login'

LOGIN\_REDIRECT\_URL = 'home'

\`\`\`

\---

\## 🔹 \*\*Static Files & Bootstrap\*\*

\### \*\*98. What is a static file URL in web development?\*\*

\*\*Answer:\*\* URL pointing to static assets (CSS, JS, images).

\---

\### \*\*99. Where should you store your static files like CSS and JavaScripts in a Django project?\*\*

\*\*Answer:\*\* In a \`static/\` folder inside each app or a global \`STATICFILES\_DIRS\`.

\---

\### \*\*100. How can large static files be effectively managed in a Django project?\*\*

\*\*Answer:\*\* Use \`whitenoise\`, CDNs, or cloud storage (e.g., AWS S3).

\---

\### \*\*101. How can you include Bootstrap in your HTML file?\*\*

\*\*Answer:\*\* Via CDN:

\`\`\`html

\`\`\`

\---

\### \*\*102. How are cards utilized in Bootstrap, and what are their key features?\*\*

\*\*Answer:\*\* Cards are flexible containers for content.

\*\*Example:\*\*

\`\`\`html

##### Title

Content

\`\`\`

\---

\### \*\*103. What are Bootstrap models, and how are they implemented?\*\*

\*\*Note:\*\* Likely meant "modals", not "models".

\*\*Answer:\*\* Modals are pop-up dialogs.

\*\*Example:\*\*

\`\`\`html

...

\`\`\`

With JavaScript or data attributes to trigger.

\---

\## 🔹 \*\*DRF (Django REST Framework)\*\*

\### \*\*104. What is the purpose of serializers in DRF?\*\*

\*\*Theory:\*\*

Convert complex data (e.g., querysets) into JSON and vice versa.

\*\*Example:\*\*

\`\`\`python

class PostSerializer(serializers.ModelSerializer):

class Meta:

model = Post

fields = '\_\_all\_\_'

\`\`\`

\---

\## 🔹 \*\*Miscellaneous\*\*

\### \*\*105. Name two commonly used web servers with Django and briefly explain their roles.\*\*

\*\*Answer:\*\*

\- \*\*Gunicorn:\*\* WSGI server for serving Django apps.

\- \*\*Nginx:\*\* Reverse proxy and serves static files.

\---

\### \*\*106. What is get\_objects\_or\_404 in Django?\*\*

\*\*Theory:\*\*

Returns object or raises 404 if not found.

\*\*Example:\*\*

\`\`\`python

post = get\_object\_or\_404(Post, id=1)

\`\`\`

\---

\### \*\*107. How do you create a view that only logged-in users can access?\*\*

\*\*Answer:\*\* Use \`@login\_required\` decorator.

\`\`\`python

from django.contrib.auth.decorators import login\_required

@login\_required

def profile(request):

return render(request, 'profile.html')

\`\`\`

\---

\### \*\*108. How do you start the development server in Django?\*\*

\*\*Answer:\*\*

\`\`\`bash

python manage.py runserver

\`\`\`

\---

\### \*\*109. Which file is responsible for defining the database settings for a Django project?\*\*

\*\*Answer:\*\* \`settings.py\`

\---

✅ \*\*All questions answered with theory and examples.\*\*