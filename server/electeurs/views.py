from django.shortcuts import render
from rest_framework import viewsets
from .models import Electeur ,Vote ,Candidature ,ElecteurVote
from .serializers import ElecteurSerializer ,CandidatureSerializer ,VoteSerializer,ElecteurVoteSerializer,UserSerializer
from django.contrib.auth.models import User

# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class =UserSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.id)

class ElecteurViewSet(viewsets.ModelViewSet):
    serializer_class =ElecteurSerializer
    queryset = Electeur.objects.all()
class VoteViewSet(viewsets.ModelViewSet):
    serializer_class =VoteSerializer
    queryset = Vote.objects.all()
class CandidatureViewSet(viewsets.ModelViewSet):
    serializer_class =CandidatureSerializer
    queryset = Candidature.objects.all()
class ElecteurVoteViewSet(viewsets.ModelViewSet):
    serializer_class =ElecteurVoteSerializer
    queryset = ElecteurVote.objects.all()