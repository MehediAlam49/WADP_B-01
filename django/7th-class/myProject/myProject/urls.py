
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student, name='studentPage' ),
    path('addStudent/', addStudent, name='addStudent' ),
    path('teacher/', teacher, name='teacherPage' ),
    path('addTeacher/', addTeacher, name='addTeacher' ),
]
