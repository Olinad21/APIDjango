from rest_framework import serializers
from .models import Dados,Dispositivo

class DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = ('id','dispositivo','leituraUV','data')

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ('id','nome','longitude','latitude')