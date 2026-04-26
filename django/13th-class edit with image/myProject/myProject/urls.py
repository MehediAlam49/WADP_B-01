
from django.contrib import admin
from django.urls import path
from myProject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student, name='student'),
    path('addStudent/', addStudent, name='addStudent'),
    path('deleteStudent/<str:myid>', deleteStudent, name='deleteStudent'),
    path('editStudent/<str:myid>', editStudent, name='editStudent'),
    path('viewStudent/<str:myid>', viewStudent, name='viewStudent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
