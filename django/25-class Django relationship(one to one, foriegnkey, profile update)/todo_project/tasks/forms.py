from django.forms import fields
from django import forms
from tasks.models import *

class productForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields='__all__'
        exclude=['created_by','total_amount']
        
        widgets={
      'due_date':forms.DateInput(attrs={
        'class':'form-control',
        'type':'date',
      })
    }
        

class ProfileForm(forms.ModelForm):
  class Meta:
    model= profileModel
    fields='__all__'
    exclude=['user']