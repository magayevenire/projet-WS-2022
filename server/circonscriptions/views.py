from django.shortcuts import render
from rest_framework import viewsets
from .models import Region ,Departement ,Commune ,Bureau
from .serializers import RegionSerializer ,DepartementSerializer ,CommuneSerializer, BureauSerializer

# Create your views here.
class RegionViewSet(viewsets.ModelViewSet):
    serializer_class =RegionSerializer
    queryset = Region.objects.all()

class DepartementViewSet(viewsets.ModelViewSet):
    serializer_class =DepartementSerializer
    queryset = Departement.objects.all()

class CommuneViewSet(viewsets.ModelViewSet):
    serializer_class =CommuneSerializer
    queryset = Commune.objects.all()
    

class BureauViewSet(viewsets.ModelViewSet):
    serializer_class =BureauSerializer
    queryset = Bureau.objects.all()