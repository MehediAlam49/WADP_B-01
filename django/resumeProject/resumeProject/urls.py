
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from resumeProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addResume/', addResume, name='addResume'),
    path('editResume/<str:myid>', editResume, name='editResume'),
    path('updateResume/', updateResume, name='updateResume'),
    path('deleteResume/<str:myid>', deleteResume, name='deleteResume'),
    path('viewResume/<str:myid>', viewResume, name='viewResume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
