
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student, name='studentpage'),
    path('addStudent/', addStudent, name='addStudent'),
    path('teacher/', teacher, name='teacher'),
]
