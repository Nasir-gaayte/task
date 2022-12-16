from django import forms 
from .models import Contactmodel, Categorymodel , Citymodel




class AddForm(forms.ModelForm):
    class Meta:
        model = Contactmodel
        fields = ("logo", "name",  "category", "city", "phone1","email")
        
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorymodel
        fields = ("__all__")     


class CityForm(forms.ModelForm):
    class Meta:
        model = Citymodel
        fields = ('__all__')    