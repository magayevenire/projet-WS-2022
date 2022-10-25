from rest_framework import serializers
from .models import Electeur ,Candidature , Vote 
from django.contrib.auth.models import User



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
        

        

class ElecteurSerializer(serializers.ModelSerializer):
    # candidatures = CandidatureSerializer(many=True,read_only=True)

    class Meta:
        model = Electeur
        fields = ("id","numero_cni",'user',"nom","prenom","date_naissance","adresse","bureau_vote","candidatures",)
        read_only_fields =("candidatures",)



class UserSerializer(serializers.ModelSerializer):
    electeur = ElecteurSerializer(many=False,read_only=True)



    class Meta:
        model = User
        fields = ('id', 'username', 'email','electeur')
