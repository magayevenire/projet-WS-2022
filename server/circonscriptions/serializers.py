from rest_framework import serializers
from .models import Region ,Departement ,Commune,Bureau  

from django.contrib.auth.models import User


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region 
        fields = ('id','nom')

class DepartementSerializer(serializers.ModelSerializer):
    region = RegionSerializer(many=False,read_only=True,)

    class Meta:
        model = Departement 
        fields = ('id','region','nom')

class CommuneSerializer(serializers.ModelSerializer):
    departement = DepartementSerializer(many=False,read_only=True,)

    class Meta:
        model = Commune 
        fields = ('id','departement','nom','nombre_inscrits')

class BureauSerializer(serializers.ModelSerializer):
    commune = CommuneSerializer(many=False,read_only=True,)
    class Meta:
        model = Bureau 
        fields = ('id','commune','numero','nombre_inscrits')

