from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myApp.views import home, createPage, readPage, updatePage, deletePage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/<str:id>/", home, name="home"),
    path("createPage/", createPage, name="createPage"),
    path("readPage/", readPage, name="readPage"),
    path("updatePage/<str:id>/", updatePage, name="updatePage"),
    path("deletePage/<str:id>/", deletePage, name="deletePage"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
