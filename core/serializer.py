from rest_framework.serializers import ModelSerializer
from .models import (
    Contactmodel,
    Citymodel,
    Categorymodel,
    )


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contactmodel
        fields = "id","logo","name","phone1","email","location_imo","location_url","desc","category","city"
    
    def to_representation(self, instance):
        rep= super(ContactSerializer,self).to_representation(instance)  
        rep['city'] = instance.city.name 
        rep['category']= instance.category.name 
        return rep
    
        

class CitySerializer(ModelSerializer):
    class Meta:
        model = Citymodel
        fields ='__all__'
   
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorymodel
        fields = '__all__'            
    
