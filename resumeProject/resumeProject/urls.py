from django.contrib import admin
from django.urls import path
from resumeProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addResume/', addResume, name='addResume'),
    path('deleteResume/<str:myid>', deleteResume, name='deleteResume'),
    path('viewResume/<str:myid>', viewResume, name='viewResume'),
    path('editResume/<str:myid>', editResume, name='editResume'),
    path('updateResume/', updateResume, name='updateResume'),
]
