from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Electeur
#
 

class Electeur(models.Model):
    user = models.OneToOneField(User,related_name='electeur',on_delete=models.CASCADE,default=None,null=True,blank=True) 

    numero_cni = models.CharField(max_length=50,null=True,blank=True)
    nom = models.CharField(max_length=50,null=True,blank=True)
    prenom = models.CharField(max_length=50,null=True,blank=True)
    date_naissance =  models.DateField(null=True,blank=True)
    Adresse = models.CharField(max_length=250,null=True,blank=True)
    # nom_centre_vote = models.CharField(max_length=50,null=True,blank=True)
    bureau_vote = models.ForeignKey("circonscriptions.Bureau",related_name='inscrits', on_delete=models.SET_NULL,null=True,blank=True)

    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)


# class parrainage(models.Model):

#     parraineur= models.ForeignKey(Electeur,related_name='parraineur', on_delete=models.CASCADE,null=True,blank=True)
#     parrainer= models.ForeignKey(Electeur,related_name='parrainer', on_delete=models.CASCADE,null=True,blank=True)
#     creation = models.DateTimeField(auto_now_add=True)
#     modifier = models.DateTimeField(auto_now=True)

class Candidature(models.Model):

    electeur= models.ForeignKey(Electeur,related_name='candidatures', on_delete=models.CASCADE,null=True,blank=True)
    elections= models.ForeignKey("elections.election", on_delete=models.CASCADE,null=True,blank=True)
    nom_parti = models.CharField(max_length=50,null=True,blank=True)

    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)



class ElecteurVote(models.Model):

    # electeur = models.ForeignKey(Electeur,related_name='canditatues', on_delete=models.CASCADE,null=True,blank=True)
    eleteur = models.ForeignKey(Electeur,related_name='votes', on_delete=models.CASCADE,null=True,blank=True)
    election = models.ForeignKey("elections.election", on_delete=models.CASCADE,null=True,blank=True)


    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)
class Vote(models.Model):

    # electeur = models.ForeignKey(Electeur,related_name='canditatues', on_delete=models.CASCADE,null=True,blank=True)
    bureau_vote = models.ForeignKey("circonscriptions.Bureau",related_name='votes', on_delete=models.SET_NULL,null=True,blank=True)
    canditaure = models.ForeignKey(Candidature, on_delete=models.CASCADE,null=True,blank=True)
    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)