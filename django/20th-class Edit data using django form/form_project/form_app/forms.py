from django import forms
from form_app.models import *

class productForm(forms.ModelForm):
    class Meta:
        model=productModel
        fields='__all__'
        exclude=['total_amount']