from django import forms

from .models import NewsModel, NewsCategoryModel


class NewsFrom(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = "__all__"
        
        
class NewsCategoryFrom(forms.ModelForm):
    class Meta:
        model = NewsCategoryModel
        fields = "__all__"