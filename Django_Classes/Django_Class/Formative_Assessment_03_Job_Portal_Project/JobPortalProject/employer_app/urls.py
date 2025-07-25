from django.urls import path
from employer_app.views import*

urlpatterns = [
    path('createJobPage/',createJobPage, name='createJobPage'),
    path('jobListPage/',jobListPage, name='jobListPage'),
    path('updateJobPage/<str:id>/',updateJobPage, name='updateJobPage'),
    path('deleteJobPage/<str:id>/',deleteJobPage, name='deleteJobPage'),
    path('jobDetailsPage/<str:id>/',jobDetailsPage, name='jobDetailsPage'),

    path('jobApplications/', allJobApplicationsPage, name='allJobApplicationsPage'),
    path('changeApplicationStatusPage/<str:id>/', changeApplicationStatusPage, name='changeApplicationStatusPage'),

]
