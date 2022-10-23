from django.db import models





class Election(models.Model):
    periode_inscription_debut = models.DateField(null=True,blank=True)
    nom = models.CharField(max_length=255,null=True,blank=True)
    periode_inscription_fin =  models.DateField(null=True,blank=True)
    periode_depot_canditature_debut =  models.DateField(null=True,blank=True)
    periode_depot_canditature_fin =  models.DateField(null=True,blank=True)
    jour_vote =  models.DateField(null=True,blank=True)
    
    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)