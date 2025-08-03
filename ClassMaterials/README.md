
# Django Creative Questions (CQ) - Questions & Answers

This document includes important CQ-style Django interview or exam questions with clear and concise answers.

---

## 🔹 Django Core Questions (1–20)

### 1. What is Django?
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.

### 2. How do you create a new project in Django?
```bash
django-admin startproject project_name
```

### 3. Which file is responsible for defining the database settings for a Django project?
`settings.py` – inside the `DATABASES` dictionary.

### 4. What is ORM in Django?
Object-Relational Mapping (ORM) allows interaction with the database using Python objects instead of raw SQL.

### 5. Purpose of the Django admin site?
Provides a built-in interface to perform CRUD operations on registered models.

### 6. What is the purpose of a URL pattern in Django?
It maps specific URLs to view functions or classes.

### 7. Difference between Project and App?
- **Project**: Full Django web application with settings.
- **App**: A module for a specific feature or functionality.

### 8. Django MVT Architecture?
- **Model**: Manages data.
- **View**: Handles business logic and returns responses.
- **Template**: HTML-based output rendering.

### 9. Which file defines database settings?
`settings.py` under the `DATABASES` section.

### 10. Where to store static files?
Inside the `static/` folder in the project or each app.

### 11. How to create a database record using ORM?
```python
obj = MyModel(field1='value')
obj.save()
```

### 12. Key features of Django
- ORM
- Admin Interface
- URL Routing
- Templates
- Form Handling
- Authentication
- Caching
- i18n support

### 13. Django Project Structure?
Includes `manage.py`, `settings.py`, `urls.py`, `models.py`, etc.

### 14. Importance of virtual environment?
To isolate dependencies per project and avoid conflicts.

### 15. Django admin interface?
Auto-generated admin panel for managing app data.

### 16. What do these commands do?
```bash
python manage.py makemigrations  # Creates migration files
python manage.py migrate         # Applies DB changes
```

### 17. Files created in a new app?
`admin.py`, `apps.py`, `models.py`, `views.py`, `tests.py`

### 18. What is a static file URL?
A URL used to access static files like CSS, JS, images.

### 19. How to display dynamic data in templates?
Use `{{ variable }}` syntax.

### 20. How to include an app in the Django project?
Add the app name in `INSTALLED_APPS` in `settings.py`.

---

## 🔹 Additional Django Commands and Concepts

### 21. How to create a new app?
```bash
python manage.py startapp app_name
```

### 22. Run development server?
```bash
python manage.py runserver
```

### 23. Create superuser?
```bash
python manage.py createsuperuser
```

### 24. Check Django version?
```bash
python -m django --version
```

### 25. Fetch all records?
```python
MyModel.objects.all()
```

### 26. Fetch by ID?
```python
MyModel.objects.get(id=1)
```

### 27. Delete a record?
```python
obj = MyModel.objects.get(id=1)
obj.delete()
```

### 28. Update a record?
```python
obj = MyModel.objects.get(id=1)
obj.name = 'New Name'
obj.save()
```

### 29. Register a model in admin?
```python
admin.site.register(MyModel)
```

### 30. Define a URL?
```python
path('home/', views.home, name='home')
```

### 31. Include URLs from another app?
```python
path('blog/', include('blog.urls'))
```

### 32. Class-based view example?
```python
from django.views import View
class MyView(View):
    def get(self, request):
        return HttpResponse('Hello')
```

### 33. Enable static files?
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

### 34. Configure media files?
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 35. Create serializer (DRF)?
```python
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
```

### 36. ForeignKey relationship?
```python
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### 37. Many-to-Many relationship?
```python
class Student(models.Model):
    courses = models.ManyToManyField(Course)
```

### 38. One-to-One relationship?
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

### 39. Create custom user model?
Extend `AbstractUser` or `AbstractBaseUser`.

### 40. Set custom user model?
```python
AUTH_USER_MODEL = 'myapp.MyUser'
```

### 41. Deploy Django to production?
Use Gunicorn, Nginx, `DEBUG=False`, and set `ALLOWED_HOSTS`.

### 42. Create and render a template?
Place in `templates/` folder, then:
```python
return render(request, 'template.html', context)
```

### 43. Add context to template?
Pass a dictionary to `render()`.

### 44. Template inheritance?
```html
{% extends 'base.html' %}
```

### 45. Use `get_object_or_404`?
```python
obj = get_object_or_404(MyModel, id=1)
```

### 46. Restrict view access?
Use `@login_required` decorator.

### 47. Connect multiple databases?
Add them to `DATABASES` in `settings.py`.

### 48. Make a field unique?
```python
email = models.EmailField(unique=True)
```

### 49. Make a field optional?
```python
bio = models.TextField(blank=True, null=True)
```

### 50. CSRF protection in forms?
Use `{% csrf_token %}` inside the form.

### 51. Serve media files in development?
```python
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Django Interview Questions & Answers

### 1. What does the 'yesno' filter do in Django templates?
**Answer:** The `yesno` filter converts a boolean value to a string. For example:
```django
{{ value|yesno:"Yes,No,Maybe" }}
```
- If `value` is `True`, it returns "Yes"
- If `value` is `False`, it returns "No"
- If `value` is `None`, it returns "Maybe"

### 2. What is the difference between path() and re_path() in Django URL patterns?
**Answer:**
- `path()` is used for simpler, non-regex based URL patterns.
- `re_path()` allows the use of regular expressions for complex patterns.
```python
# path()
path('home/', views.home)

# re_path()
re_path(r'^home/$', views.home)
```

### 3. What is the purpose of a URL pattern in Django?
**Answer:** URL patterns map URLs to views. It tells Django which function to call when a particular URL is requested.

### 4. Explain the purpose of the Django admin site?
**Answer:** The Django admin site provides a web-based interface to manage the application's data and models.

### 5. Which file is responsible for defining the database settings for a Django project?
**Answer:** The `settings.py` file contains the `DATABASES` dictionary for database configurations.

### 6. What does the 'date' filter do in Django templates?
**Answer:** Formats a date according to the given format string.
```django
{{ my_date|date:"D M Y" }}
```

### 7. What is a Django form and what is its purpose?
**Answer:** Django forms are used to handle user input and validation.
```python
class ContactForm(forms.Form):
    name = forms.CharField()
```

### 8. How is a Django form submitted in a template?
**Answer:**
```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

### 9. What is a static file URL in web development?
**Answer:** A static file URL is the path through which static resources (CSS, JS, images) are served.

### 10. What is the purpose of serializers in DRF?
**Answer:** Serializers convert complex data (querysets, model instances) to native Python datatypes for rendering into JSON, XML, etc.

### 11. Which file is responsible for defining the database settings for a Django project?
**Answer:** `settings.py` file under the project directory.

### 12. Where should you store your static files like CSS and JavaScripts in a Django project?
**Answer:** Inside an app-level `static/` directory or in a global `static/` folder defined in `STATICFILES_DIRS`.

### 13. How is a URL pattern defined in Django's `urls.py` file?
**Answer:**
```python
from django.urls import path
urlpatterns = [
    path('home/', views.home_view, name='home'),
]
```

### 14. What is the purpose of the `reverse()` function in Django with respect to URLs?
**Answer:** It returns the URL path based on the name of the URL pattern.
```python
reverse('home')  # returns '/home/'
```

### 15. What does the 'date' filter do in Django templates?
**Answer:** Formats a date value. Example:
```django
{{ some_date|date:"Y-m-d" }}
```

### 16. What is the purpose of the 'length' filter in Django templates?
**Answer:** Returns the number of items in a list or characters in a string.
```django
{{ my_list|length }}
```

### 17. How do you create a new database record (object) using Django ORM?
**Answer:**
```python
Book.objects.create(title="Django", author="XYZ")
```

### 18. How do you perform a bulk delete operation on multiple records in Django models?
**Answer:**
```python
Book.objects.filter(author='XYZ').delete()
```

### 19. How do you define a form class in Django?
**Answer:**
```python
class BookForm(forms.Form):
    title = forms.CharField()
```

### 20. How do you access form data submitted through POST method in a Django view?
**Answer:**
```python
if request.method == "POST":
    form = BookForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
```

### 22. How can you include Bootstrap in your HTML file?
**Answer:**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
```

### 23. What is the role of the `is_authenticated` attribute in Django user authentication?
**Answer:** Checks if the current user is logged in.
```python
if request.user.is_authenticated:
    # show profile
```

### 24. What are Bootstrap modals, and how are they implemented?
**Answer:** Bootstrap modals are pop-up dialogs. Example:
```html
<div class="modal fade" id="myModal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">Modal Title</div>
      <div class="modal-body">Modal body</div>
    </div>
  </div>
</div>
```

### 25. Name two commonly used web servers with Django and briefly explain their roles.
**Answer:**
- **Gunicorn:** Production-level WSGI server
- **Django's runserver:** For development/testing only

### 26. What is `get_object_or_404` in Django?
**Answer:** It retrieves an object or raises 404 if not found.
```python
book = get_object_or_404(Book, pk=1)
```

### 27. What is a view in Django?
**Answer:** A view is a Python function or class that handles web requests and returns web responses.

### 28. How does Django’s authentication system work?
**Answer:** It provides user authentication, login, logout, password management, and permission checking.

### 29. What is Django Admin, how is it used?
**Answer:** Django Admin is a backend interface to manage models. You register models in `admin.py` to use it.

### 30. How does Django’s ORM help manage relationships between models?
**Answer:** It uses ForeignKey, OneToOneField, and ManyToManyField to define relationships.

### 31. How do you create a new record in the database using Django ORM?
**Answer:**
```python
Author.objects.create(name='John Doe')
```

### 32. What is a model in Django?
**Answer:** A model is a Python class that defines the structure of your database tables.

### 33. What is the use of manage.py in Django?
**Answer:** `manage.py` is a command-line tool to interact with your project (runserver, makemigrations, etc.)

### 34. What is the purpose of Meta class in a Django model?
**Answer:** Meta defines metadata like ordering, verbose_name, and db_table.
```python
class Meta:
    ordering = ['name']
```

### 35. How do you create a view that only logged-in users can access?
**Answer:** Use the `@login_required` decorator.
```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

### 36. How do you use a for loop in Django templates?
**Answer:**
```django
{% for item in items %}
    {{ item }}
{% endfor %}
```

### 37. What is a template inheritance in Django?
**Answer:** Template inheritance lets you build a base layout and extend it in child templates.
```django
<!-- base.html -->
{% block content %}{% endblock %}

<!-- home.html -->
{% extends 'base.html' %}
{% block content %} Home Page {% endblock %}
```

### 38. How do you delete a record in Django ORM?
**Answer:**
```python
book = Book.objects.get(id=1)
book.delete()
```

## Django Re-Assessment Questions & Answers

### 1. What is a Django model in the context of web development?
**Answer:** A Django model is a Python class that maps to a database table and is used to define and manipulate structured data.

### 2. How can you perform database migrations in Django?
**Answer:**
```bash
python manage.py makemigrations  # Creates migration files
python manage.py migrate         # Applies migration to the database
```

### 3. Which Django command is used to generate the necessary database schema based on the model?
**Answer:** `python manage.py migrate`

### 4. What is the purpose of the auto_now_add option in a Django DateTimeField?
**Answer:** It sets the field to the current date and time when the object is first created.

### 5. What is the purpose of the {% block %} tag in Django templates?
**Answer:** It allows you to define a block of content that child templates can override.

### 6. Which template tag is used to display the URL for a named URL pattern in Django templates?
**Answer:**
```django
{% url 'name_of_the_url_pattern' %}
```

### 7. Which template tag is used to perform if-else logic in Django templates?
**Answer:**
```django
{% if condition %}
    Do something
{% else %}
    Do something else
{% endif %}
```

### 8. How do you start the development server in Django?
**Answer:** `python manage.py runserver`

### 9. Which template tag is used for escaping HTML content in Django templates?
**Answer:** `{{ variable|escape }}`

### 10. How can you handle form submissions in Django views?
**Answer:** By using `request.POST` inside views to access submitted data.

---

### 11. What is the purpose and use of the save() function in Django?
**Answer:** It saves the current instance of a model to the database.

### 12. How are cards utilized in Bootstrap, and what are their key features?
**Answer:** Cards are used to display content with padding, border, and shadow. They're responsive and used for layout containers.

### 13. How can large static files be effectively managed in a Django project?
**Answer:** Use the `collectstatic` command to gather static files into a single location for deployment.

### 14. What are the advantages of using URL patterns in Django?
**Answer:** URL patterns map URLs to views, improving routing and organization.

### 15. How are template views implemented in Django's Class-Based Views (CBVs)?
**Answer:** By using `TemplateView`:
```python
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'
```

### 16. How can conditional logic be used to display "Yes" or "No" in a Django template?
**Answer:**
```django
{{ value|yesno:"Yes,No" }}
```

---

### 17. What is Django?
**Answer:** A high-level Python framework for rapid web development.

### 18. What are the main features of Django?
**Answer:** ORM, admin interface, authentication, templates, routing, scalability.

### 19. What is the default database supported by Django?
**Answer:** SQLite

### 20. How do you create a Django project?
**Answer:** `django-admin startproject project_name`

### 21. What is the use of manage.py?
**Answer:** A command-line tool for managing the Django project (runserver, migrate, etc.).

### 22. How do you start a new app in a Django project?
**Answer:** `python manage.py startapp app_name`

### 23. What is the difference between a project and an app in Django?
**Answer:** A project contains global settings; apps are components handling specific features.

### 24. What is the role of settings.py in a Django project?
**Answer:** Holds all configuration including DB, static files, middleware, installed apps, etc.

---

### 25. What is a model in Django?
**Answer:** A Python class that maps to a database table.

### 26. How do you define a model in Django?
**Answer:**
```python
class Book(models.Model):
    title = models.CharField(max_length=100)
```

### 27. What command is used to apply changes to the database after modifying models?
**Answer:** `python manage.py migrate`

### 28. What are makemigrations and migrate commands in Django?
**Answer:** `makemigrations` generates migration files, `migrate` applies them to the database.

### 29. What is the purpose of Meta class in a Django model?
**Answer:** It defines metadata like ordering, verbose_name, and table name.

### 30. How can you retrieve all records from a model?
**Answer:**
```python
Book.objects.all()
```

### 31. What is the difference between get() and filter() in Django QuerySet?
**Answer:**
- `get()` returns a single object or raises error.
- `filter()` returns a queryset (list of objects).

### 32. What is the purpose of the models.py file in a Django app?
**Answer:** It's where all database models are defined.

### 33. What is the significance of the id field in Django models?
**Answer:** It's the default primary key field added by Django.

### 34. What is the default primary key field in Django models?
**Answer:** An `id` field of type `AutoField`.

### 35. How do you define a field as a primary key in Django?
**Answer:**
```python
id = models.IntegerField(primary_key=True)
```

### 36. Name some commonly used field types in Django models.
**Answer:** CharField, TextField, IntegerField, DateField, DateTimeField, ForeignKey

### 37. What is the purpose of CharField and TextField in Django models?
**Answer:**
- `CharField`: For short strings with max_length.
- `TextField`: For long text.

### 38. How does ForeignKey work in Django models?
**Answer:** It creates a many-to-one relationship to another model.

### 39. What is a ManyToManyField in Django, and when should you use it?
**Answer:** It defines a many-to-many relationship. Use when multiple records relate both ways.

### 40. What is the difference between DateField and DateTimeField?
**Answer:** `DateField` stores only the date, `DateTimeField` stores both date and time.

### 41. What is the purpose of the Meta class in a Django model?
**Answer:** Defines model-level options like ordering, table name.

### 42. How do you define a table name for a model using Meta?
**Answer:**
```python
class Meta:
    db_table = 'custom_table_name'
```

### 43. How can you make a model field unique?
**Answer:** Add `unique=True` to the field definition.

### 44. What is the use of db_index=True in a model field?
**Answer:** It creates an index on that field for faster querying.

### 45. How can you order querysets by default for a model?
**Answer:**
```python
class Meta:
    ordering = ['fieldname']
```

### 46. What is the difference between OneToOneField, ForeignKey, and ManyToManyField?
**Answer:**
- `OneToOneField`: One-to-one relationship.
- `ForeignKey`: Many-to-one relationship.
- `ManyToManyField`: Many-to-many relationship.

### 47. How do you set up a self-referential ForeignKey in a model?
**Answer:**
```python
parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
```

### 48. How do you define a related name for a ForeignKey field?
**Answer:**
```python
author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
```
