from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Citymodel(models.Model):
    name=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name

    


class Categorymodel(models.Model):
    name = models.CharField(max_length=100)
    city=models.ForeignKey(Citymodel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Contactmodel(models.Model):
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=False,blank=False)
    category=models.ForeignKey(Categorymodel,on_delete=models.CASCADE)
    city=models.ForeignKey(Citymodel,on_delete=models.CASCADE)
    phone1 = models.IntegerField(null=False,blank=False)
    phone2 = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"name:{self.name}phone{self.phone1}-{self.phone2}"