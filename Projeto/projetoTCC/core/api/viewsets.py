from ..models import Dados,Dispositivo
from rest_framework import viewsets
from ..serializers import DadosSerializer,DispositivoSerializer
from django.shortcuts import render

class DadosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows data to be viewed or edited.
    """
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dispositive to be viewed or edited.
    """
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer