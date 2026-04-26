
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student, name='student'),
    path('addStudent/', addStudent, name='addStudent'),
    path('deleteStudent/<str:myid>', deleteStudent, name='deleteStudent'),
    path('editStudent/<str:myid>', editStudent, name='editStudent'),
    path('viewStudent/<str:myid>', viewStudent, name='viewStudent'),
    path('updateStudent/', updateStudent, name='updateStudent'),
    path('teacher/', teacher, name='teacher'),
    path('management/', management, name='management'),
    path('allData/', allData, name='allData'),
]
