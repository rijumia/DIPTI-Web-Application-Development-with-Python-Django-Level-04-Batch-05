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