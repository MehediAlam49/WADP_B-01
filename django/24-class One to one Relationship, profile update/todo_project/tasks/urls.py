from django.urls import path
from tasks.views import *

urlpatterns = [
    path('', register_page, name='register_page'),
    path('login-page/', login_page, name='login_page'),
    path('logout-page/', logout_page, name='logout_page'),
    
    path('home/', home, name='home'),
    path('task-list/', task_list, name='task_list'),
    path('add-task/', add_task, name='add_task'),
    path('edit-task/<str:id>', edit_task, name='edit_task'),
    path('view-task/<str:id>', view_task, name='view_task'),
    path('delete-task/<str:id>', delete_task, name='delete_task'),
    
    path('profile/', profile_page, name='profile_page'),
    path('update-profile/', update_profile, name='update_profile'),
]
