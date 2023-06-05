from rest_framework.serializers import ModelSerializer
from .models import NewsCategoryModel,NewsModel


class NewsSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields ='__all__'
        
        
    def to_representation(self, instance):
        rep= super(NewsSerializer,self).to_representation(instance)
        rep['category'] = instance.category.name
        return rep
    
    
class NewsCateSerializer(ModelSerializer):
    class Meta:
        model = NewsCategoryModel
        fields ='__all__'
        