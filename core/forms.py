from django import forms 
from .models import Contactmodel, Categorymodel , Citymodel, PromoModel




class AddForm(forms.ModelForm):
    class Meta:
        model = Contactmodel
        fields = ("logo", "name", "category", "city", "phone1","email","location_imo","location_url")
        
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorymodel
        fields = ("__all__")     


class CityForm(forms.ModelForm):
    class Meta:
        model = Citymodel
        fields = ('__all__')    
        
        
class PromoForm(forms.ModelForm):
    class Meta:
        model =   PromoModel
        fields = ('__all__')       