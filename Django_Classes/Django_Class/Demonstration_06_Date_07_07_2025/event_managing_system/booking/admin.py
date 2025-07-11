from django.contrib import admin
from booking.models import EventBookingModel, EventUserModel

admin.site.register(EventUserModel)
admin.site.register(EventBookingModel)
