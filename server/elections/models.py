from django.db import models

# Create your models here.
 
class Periode(models.Model):
    debut =  models.DateField()
    fin = models.DateField()



class Election(models.Model):
    periode_inscription =  models.ForeignKey(Periode,related_name='periode_inscription', on_delete=models.SET_NULL,null=True,blank=True)
    periode_depot_canditature =  models.ForeignKey(Periode,related_name='periode_depot_canditature', on_delete=models.SET_NULL,null=True,blank=True)
    jour_vote =  models.DateField(null=True,blank=True)
    
    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)