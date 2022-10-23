from django.shortcuts import render
from rest_framework import viewsets
from .models import Electeur ,Vote ,Candidature 
from .serializers import ElecteurSerializer ,CandidatureSerializer ,VoteSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class =UserSerializer
    queryset = User.objects.all()


    @action(detail=False)
    def me(self, request):
        user = self.queryset.get(pk=self.request.user.id)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ElecteurViewSet(viewsets.ModelViewSet):
    serializer_class =ElecteurSerializer
    queryset = Electeur.objects.all()
class VoteViewSet(viewsets.ModelViewSet):
    serializer_class =VoteSerializer
    queryset = Vote.objects.all()
class CandidatureViewSet(viewsets.ModelViewSet):
    serializer_class =CandidatureSerializer
    queryset = Candidature.objects.all()
