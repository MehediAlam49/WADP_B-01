from django.urls import path
from tasks.views import *

urlpatterns = [
    path('', register_page, name='register_page'),
    path('login-page/', login_page, name='login_page'),
    path('logout-page/', logout_page, name='logout_page'),
    
    path('home/', home, name='home'),
    path('product-list/', product_list, name='product_list'),
    path('add-product/', add_product, name='add_product'),
    path('edit-product/<str:id>', edit_product, name='edit_product'),
    path('view-product/<str:id>', view_product, name='view_product'),
    path('delete-product/<str:id>', delete_product, name='delete_product'),
    
    path('profile/', profile_page, name='profile_page'),
    path('update-profile/', update_profile, name='update_profile'),
]
