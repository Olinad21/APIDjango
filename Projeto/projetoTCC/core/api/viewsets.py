from rest_framework.filters import SearchFilter

from ..models import Dados,Dispositivo
from rest_framework import viewsets
from ..serializers import DadosSerializer,DispositivoSerializer
from django.shortcuts import render

class DadosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows data to be viewed or edited.
    """
    filter_backends = (SearchFilter,)
    filter_fields = ('leituraUV', 'data','dispositivo__id','dispositivo__nome')
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dispositive to be viewed or edited.
    """
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer