from rest_framework import serializers
from .models import Election ,Periode 


class PeriodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Periode
        fields = ("__all__")
        
class ElectionSerializer(serializers.ModelSerializer):
    periode_inscription =  PeriodeSerializer(many=False,)
    periode_depot_canditature =  PeriodeSerializer(many=False,)
    
    class Meta:
        model = Election
        fields = ("__all__")