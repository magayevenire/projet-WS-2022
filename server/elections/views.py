from django.shortcuts import render
from rest_framework import viewsets

from electeurs.models import Candidature
from .models import Election 
from .serializers import ElectionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from circonscriptions.models import Bureau
from electeurs.models import Vote
from electeurs.serializers import VoteSerializer ,CandidatureSerializer
from django.core import serializers
from django.db.models import Count ,Q
from django.core import serializers
from django.http import HttpResponse ,JsonResponse

# Create your views here.
class ElectionViewSet(viewsets.ModelViewSet):
    serializer_class =ElectionSerializer
    queryset = Election.objects.all()

    @action(detail=False)
    def region(self, request,pk=None):

        # client = self.queryset.get(user=self.request.user.id)
        serializer = self.get_serializer( self.queryset)

        

        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=True)
    def bureau(self, request,pk=None):
        
        id= request.GET.get('id', None)
        if(id):
            election = self.queryset.get(pk=pk)

            votes = Vote.objects.filter(bureau_vote=id,candidature__election=election)
            total = votes.count()
            candidatures = Candidature.objects.filter(election=election)
            candidatures = candidatures.annotate(votes= Count('vote',filter=Q(vote__bureau_vote=id))).values()

            # serialiser = CandidatureSerializer(candidatures, many=True)
            

            return Response({"total":total,"candidature":list(candidatures)}, status=status.HTTP_200_OK)
        else :
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True)
    def commune(self, request,pk=None):
        
        id= request.GET.get('id', None)
        if(id):
            election = self.queryset.get(pk=pk)

            votes = Vote.objects.filter(bureau_vote__commune=id,candidature__election=election)
            total = votes.count()
            candidatures = Candidature.objects.filter(election=election)
            candidatures = candidatures.annotate(votes= Count('vote',filter=Q(vote__bureau_vote__commune=id))).values()
            return Response({"total":total,"candidature":list(candidatures)}, status=status.HTTP_200_OK)
        else :
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def departement(self, request,pk=None):
        
        id= request.GET.get('id', None)
        if(id):
            election = self.queryset.get(pk=pk)

            votes = Vote.objects.filter(bureau_vote__commune__departement=id,candidature__election=election)
            total = votes.count()
            candidatures = Candidature.objects.filter(election=election)
            candidatures = candidatures.annotate(votes= Count('vote',filter=Q(vote__bureau_vote__commune__departement=id))).values()
            return Response({"total":total,"candidature":list(candidatures)}, status=status.HTTP_200_OK)
        else :
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def region(self, request,pk=None):
        
        id= request.GET.get('id', None)
        if(id):
            election = self.queryset.get(pk=pk)

            votes = Vote.objects.filter(bureau_vote__commune__departement__region=id,candidature__election=election)
            total = votes.count()
            candidatures = Candidature.objects.filter(election=election)
            candidatures = candidatures.annotate(votes= Count('vote',filter=Q(vote__bureau_vote__commune__departement__region=id))).values()
            return Response({"total":total,"candidature":list(candidatures)}, status=status.HTTP_200_OK)
        else :
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def total(self, request,pk=None):
        
        election = self.queryset.get(pk=pk)
        votes = Vote.objects.filter(candidature__election=election)
        total = votes.count()
        candidatures = Candidature.objects.filter(election=election)
        candidatures = candidatures.annotate(votes= Count('vote')).values()
        return Response({"total":total,"candidature":list(candidatures)}, status=status.HTTP_200_OK)
    
    # @action(detail=True)
    # def simulation(self, request,pk=None):
        
    #     election = self.queryset.get(pk=pk)
    #     bureaux  =  Bureau.objects.all()
    #     for bureau in bureaux :
    #         for
    #         votes = Vote.objects.create(
    #             electeur= 1,
    #             bureau_vote = bureau 
    #         )
    #     total = votes.count()

        
    #     candidatures = Candidature.objects.filter(election=election)
    #     candidatures = candidatures.annotate(votes= Count('vote')).values()
    #     return Response({"total":total,"candidature":list(candidatures)}, status=status.HTTP_200_OK)
    
