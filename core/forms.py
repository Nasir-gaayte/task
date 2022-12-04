from django import forms 
from .models import Contactmodel




class AddForm(forms.ModelForm):
    class Meta:
        model = Contactmodel
        fields = ("name", "category", "city", "phone1","email")
    