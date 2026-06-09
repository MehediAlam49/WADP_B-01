from django.urls import path
from form_app.views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add-product/', add_product, name='add_product'),
    path('edit-product/<str:p_id>', edit_product, name='edit_product'),
]
