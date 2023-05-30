from rest_framework.serializers import ModelSerializer
from .models import (
    Contactmodel,
    Citymodel,
    Categorymodel,
    )


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contactmodel
        fields = '__all__'

class CitySerializer(ModelSerializer):
    class Meta:
        model = Citymodel
        fields ='__all__'
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorymodel
        fields = '__all__'            
    
