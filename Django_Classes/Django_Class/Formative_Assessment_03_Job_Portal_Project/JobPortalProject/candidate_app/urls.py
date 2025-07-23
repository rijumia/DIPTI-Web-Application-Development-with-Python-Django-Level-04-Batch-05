from django.urls import path
from candidate_app.views import *


urlpatterns = [
    path('appliedJobList/',appliedJobList,name='appliedJobList'),
    path('applyJob/<str:id>/',applyJob,name='applyJob'),
]