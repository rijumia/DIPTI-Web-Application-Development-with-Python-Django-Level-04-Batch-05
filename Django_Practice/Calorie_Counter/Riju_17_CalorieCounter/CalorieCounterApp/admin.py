from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUserAuthModel)
admin.site.register(UserProfileModel)
admin.site.register(DailyConsumedModel)
admin.site.register(TotalConsumedModel)