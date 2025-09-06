
from django.contrib import admin
from django.urls import path
from managecash.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signuppage, name='signup'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', homepage, name='home'),
    path('addcash/', addcashpage, name='addcash'),
    path('addexpence/', addexpence, name='addexpence'),
    path('editcash/<int:id>/', editcashpage, name='editcash'),
    path('editexpence/<int:id>/', editexpence, name='editexpence'),
    path('deletecash/<int:id>/', deletecash, name='deletecash'),
    path('deleteexpence/<int:id>/', deleteexpence, name='deleteexpence'),
    path('transaction/', transaction, name='transaction'),
    path('profile/', profile, name='profile'),
    path('editprofile/', editprofile, name='editprofile'),
    path('changepassword/', changepass, name='changepassword'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
