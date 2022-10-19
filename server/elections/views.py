from django.shortcuts import render
from rest_framework import viewsets
from .models import Election 
from .serializers import ElectionSerializer

# Create your views here.
class ElectionViewSet(viewsets.ModelViewSet):
    serializer_class =ElectionSerializer
    queryset = Election.objects.all()