from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('', user_register, name='user_register'),
    path('login-page/', login_page, name='login_page'),
    path('signout-page/', signout, name='signout'),
    path('home/', home, name='home'),
]
