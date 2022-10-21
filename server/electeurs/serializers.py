from rest_framework import serializers
from .models import Electeur ,Candidature , Vote ,ElecteurVote
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('__all__')



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
        

class ElecteurSerializer(serializers.ModelSerializer):
    # candidatures = CandidatureSerializer(many=True,read_only=True)
    # votes = ElecteurVoteSerializer(many=True,read_only=True)

    class Meta:
        model = Electeur
        fields = ("id","numero_cni",'user',"nom","prenom","date_naissance","Adresse","bureau_vote","candidatures","votes")
        



class UserSerializer(serializers.ModelSerializer):
    electeur = ElecteurSerializer(many=False,read_only=True)



    class Meta:
        model = User
        fields = ('id', 'username', 'email','electeur')
