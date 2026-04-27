
from django.contrib import admin
from django.urls import path
from publication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book, name='book'),
    path('addBook/', addBook, name='addBook'),
]
