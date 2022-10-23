from django.db import models
from django.db.models import Avg, Count, Min, Sum


class Circonscription(models.Model):
    nom = models.CharField(max_length=100)
    position_geographique = models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        abstract = True



class Region(Circonscription):
    # class Meta:
    #     unique_together = ('nom', )
    @property
    def nombre_inscrits(self):
        return self.departements.aggregate(Sum('nombre_inscrits'))

    def __str__(self):
        return f"{self.nom}"

class Departement(Circonscription):

    region= models.ForeignKey(Region,related_name='departements', on_delete=models.CASCADE,null=True,blank=True)
    # class Meta:
    #     unique_together = ('nom', 'region',)

    @property
    def nombre_inscrits(self):
        return self.communes.aggregate(Sum('nombre_inscrits'))
    def __str__(self):
        return f"{self.nom} -  {self.region}"

class Commune(Circonscription):
    departement= models.ForeignKey(Departement,related_name='communes', on_delete=models.CASCADE,null=True,blank=True)
    # class Meta:
    #     unique_together = ('nom', 'departement',)
    @property
    def nombre_inscrits(self):
        # print(self.bureaux.aggregate)
        return "self.bureaux.aggregate(Sum('nombre_inscrits'))"

    def __str__(self):
        return f"{self.nom} -  {self.departement}"

# class Centre(Circonscription):

#     commune= models.ForeignKey(Commune,related_name='bureaux', on_delete=models.CASCADE,null=True,blank=True)
#     numero = models.PositiveIntegerField()
#     class Meta:
#         unique_together = ('commune', 'numero',)

#     @property
#     def nombre_inscrits(self):
#         return self.inscrits.count()

class Bureau(models.Model):

    commune= models.ForeignKey(Commune,related_name='bureaux', on_delete=models.CASCADE,null=True,blank=True)
    numero = models.PositiveIntegerField()
    # class Meta:
    #     unique_together = ('commune', 'numero',)

    @property
    def nombre_inscrits(self):
        return self.inscrits.count()
    

    def __str__(self):
        return f"{self.commune} -  {self.numero}"