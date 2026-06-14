from django import forms
from form_app.models import *

class productForm(forms.ModelForm):
    class Meta:
        model=productModel
        fields='__all__'
        exclude=['total_amount']
        
    #     widgets={
    #         "product_name":forms.TextInput(attrs={"class":"form-control"})
    #     }
        
        
        
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     for f in self.fields.values():
    #         f.widget.attrs.update({"class":"form-control"})
    