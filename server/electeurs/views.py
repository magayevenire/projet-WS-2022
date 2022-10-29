from django.shortcuts import render
from rest_framework import viewsets
from .models import Electeur ,Vote ,Candidature 
from elections.models import Election
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
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     else:
             
    #         errors = [ f"{field} - {detail[0]}"  for field ,detail in serializer.errors.items()]
        
    #         return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class VoteViewSet(viewsets.ModelViewSet):
    serializer_class =VoteSerializer
    queryset = Vote.objects.all()

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            headers = self.get_success_headers(serializer.data)
            elections = Electeur.objects.get(user=request.user.id).elections
            election = Candidature.objects.get(pk=request.data['candidature']).election.pk
            if (elections and  election and (election in elections)) :
                return Response({"already vote"}, status=status.HTTP_400_BAD_REQUEST)
            self.perform_create(serializer)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
             
            # errors = [ f"{field} - {detail[0]}"  for field ,detail in serializer.errors.items()]
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CandidatureViewSet(viewsets.ModelViewSet):
    serializer_class =CandidatureSerializer
    queryset = Candidature.objects.all()
