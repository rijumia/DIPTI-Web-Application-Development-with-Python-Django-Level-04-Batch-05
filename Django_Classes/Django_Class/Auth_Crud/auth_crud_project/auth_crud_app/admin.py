from django.contrib import admin
from auth_crud_app.models import CustomUserModel, ProductModel
from django.contrib.auth.admin import UserAdmin

class userModel(UserAdmin):
    list_display = ['username', 'email', 'user_type']
    
admin.site.register(CustomUserModel,userModel)
admin.site.register(ProductModel)    


