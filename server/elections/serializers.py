from rest_framework import serializers
from .models import Election 

from electeurs.models import Candidature ,Electeur
class ElecteurSerializer(serializers.ModelSerializer):


    class Meta:
        model = Electeur
        fields = ("id","numero_cni","nom","prenom","date_naissance","Adresse")


class CandidatureSerializer(serializers.ModelSerializer):
    candidat = ElecteurSerializer(many=False,read_only=True)

    class Meta:
        model = Candidature
        fields = ("id","candidat","nom_parti","nom_parti","creation")



class ElectionSerializer(serializers.ModelSerializer):
    candidats = CandidatureSerializer(many=True,read_only=True)


    class Meta:
        model = Election
        fields = ("periode_inscription_debut",
        "nom",
        "periode_inscription_fin",
        "periode_depot_canditature_debut",
        "periode_depot_canditature_fin",
        "jour_vote",
        "creation",
        "candidats"
        )

