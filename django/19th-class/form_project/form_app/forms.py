from django import forms
from form_app.models import *

class productForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields='__all__'
        