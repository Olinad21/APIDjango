from rest_framework import serializers
from .models import Dados,Dispositivo

class DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = ('dispositivo','leituraUV','data')

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ('nome','longitude','latitude')