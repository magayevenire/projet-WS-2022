from rest_framework import serializers
from .models import Electeur ,Candidature , Vote ,ElecteurVote
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','email',)


class ElecteurSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=True,)
    class Meta:
        model = Electeur
        fields = ("id","user","numero_cni","nom","prenom","date_naissance","Adresse","bureau_vote")
        


class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = ("__all__")

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("__all__")
        
class ElecteurVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElecteurVote
        fields = ("__all__")
        
  