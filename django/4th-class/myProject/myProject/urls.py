
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name='home'),
    path('about/', aboutpage, name='about'),
    path('news/', newspage, name='news'),
    path('contact/', contactpage, name='contact'),
]
