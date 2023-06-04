from django.db import models


class NewsCategoryModel(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
    



class NewsModel(models.Model):
    category = models.ForeignKey(NewsCategoryModel,on_delete=models.CASCADE)
    imgUrl = models.ImageField(blank=True,null=True)
    newsTitel = models.CharField(max_length=150,blank=True ,null=True)
    by=models.CharField(max_length=50,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
    
    class Mate:
        
        fields = '__all__'
    
    
    def __str__(self):
        return self.newsTitel
    
    
    
