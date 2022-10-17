from django.db import models
from django.db.models import Avg, Count, Min, Sum


class Circonscription(models.Model):
    nom = models.CharField(max_length=100)
    position_geographique = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Region(Circonscription):

    @property
    def nombre_inscrits(self):
        return self.departements.aggregate(Sum('nombre_inscrits'))

class Departement(Circonscription):

    region= models.ForeignKey(Region,related_name='departements', on_delete=models.CASCADE,null=True,blank=True)

    @property
    def nombre_inscrits(self):
        return self.communes.aggregate(Sum('nombre_inscrits'))

class Commune(Circonscription):
    departement= models.ForeignKey(Departement,related_name='communes', on_delete=models.CASCADE,null=True,blank=True)

    @property
    def nombre_inscrits(self):
        return self.bureaux.aggregate(Sum('nombre_inscrits'))

# class Centre(Circonscription):

#     commune= models.ForeignKey(Commune,related_name='bureaux', on_delete=models.CASCADE,null=True,blank=True)
#     numero = models.PositiveIntegerField()
#     class Meta:
#         unique_together = ('commune', 'numero',)

#     @property
#     def nombre_inscrits(self):
#         return self.inscrits.count()

class Bureau(Circonscription):

    commune= models.ForeignKey(Commune,related_name='bureaux', on_delete=models.CASCADE,null=True,blank=True)
    numero = models.PositiveIntegerField()
    class Meta:
        unique_together = ('commune', 'numero',)

    @property
    def nombre_inscrits(self):
        return self.inscrits.count()
    
