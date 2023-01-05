import django_filters
from core.models import Contactmodel

class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contactmodel
      
        fields = {
            'name':['istartswith'],
            'category':['exact'],
            'city':['exact'],
        }