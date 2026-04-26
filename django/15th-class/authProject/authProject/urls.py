
from django.contrib import admin
from django.urls import path
from authProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signoutPage/', signoutPage, name='signoutPage'),
    path('dashboard/', dashboard, name='dashboard'),
]
