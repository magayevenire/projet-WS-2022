from enum import unique
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Electeur
#
 

class Electeur(models.Model):
    user = models.OneToOneField(User,related_name='electeur',on_delete=models.CASCADE,default=None,null=True,blank=True) 

    numero_cni = models.CharField(max_length=50,unique=True)
    nom = models.CharField(max_length=50,null=True,blank=True)
    prenom = models.CharField(max_length=50,null=True,blank=True)
    date_naissance =  models.DateField(null=True,blank=True)
    adresse = models.CharField(max_length=250,null=True,blank=True)
    # nom_centre_vote = models.CharField(max_length=50,null=True,blank=True)
    bureau_vote = models.ForeignKey("circonscriptions.Bureau",related_name='inscrits', on_delete=models.CASCADE)

    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.prenom} -  {self.nom}"


# class parrainage(models.Model):

#     parraineur= models.ForeignKey(Electeur,related_name='parraineur', on_delete=models.CASCADE,null=True,blank=True)
#     parrainer= models.ForeignKey(Electeur,related_name='parrainer', on_delete=models.CASCADE,null=True,blank=True)
#     creation = models.DateTimeField(auto_now_add=True)
#     modifier = models.DateTimeField(auto_now=True)

class Candidature(models.Model):

    candidat= models.ForeignKey(Electeur,related_name='candidatures', on_delete=models.CASCADE,null=True,blank=True)
    election= models.ForeignKey("elections.election",related_name='candidats',on_delete=models.CASCADE,null=True,blank=True)
    nom_parti = models.CharField(max_length=50,null=True,blank=True)

    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)

    @property
    def votes(self):
        return self.vote.count()

    @property
    def pourcentage(self):
      
        print(self.election.candidats)
        return "self.election.candidats.votes.count()"

    def __str__(self):
        return f"{self.nom_parti} -  {self.candidat.prenom} -  {self.candidat.nom}"




class Vote(models.Model):

    electeur = models.ForeignKey(Electeur,related_name='votes', on_delete=models.CASCADE)
    bureau_vote = models.ForeignKey("circonscriptions.Bureau",related_name='suffrages', on_delete=models.CASCADE)
    candidature = models.ForeignKey(Candidature,related_name='vote', on_delete=models.CASCADE)
    creation = models.DateTimeField(auto_now_add=True)
    modifier = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('electeur', 'candidature')
    def __str__(self):
        return f"{self.canditaure}"