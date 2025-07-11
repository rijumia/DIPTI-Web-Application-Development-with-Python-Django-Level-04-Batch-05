from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from recipeApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list/',recipeList, name='recipeList'),
    path('add/', addRecipe, name='addRecipe'),
    path('edit/<str:id>/', editRecipe, name='editRecipe'),
    path('delete/<str:id>/', deleteRecipe, name='deleteRecipe'),
    path('view/<str:id>/', viewRecipe, name='viewRecipe')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
