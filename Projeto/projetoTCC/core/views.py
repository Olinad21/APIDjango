from datetime import datetime

from django.utils import timezone
from django.shortcuts import render
from .models import Dados, Dispositivo
from django.http import HttpResponse,JsonResponse
from django .template import loader


#from .serializers import DadosSerializer,DispositivoSerializer


def teste(request):
    list1 = Dados.objects.filter(dispositivo.nome='DF')
    list2= Dispositivo.objects.get(pk=1)
    lista = list1 | list2
    now = datetime.now
    #hoje=now.day

    listO = Dados.objects.select_related('dispositivo').get(id=3)
    lat = Dispositivo.objects.get(pk=1)
    list = Dados.objects.select_related('dispositivo').get(dispositivo=3)
    # list = Dados.objects.filter(data=3)
    ult = Dados.objects.latest('data')

    api_key = 'AIzaSyC-gwBjleF-ixYwe5NhiF6TMVIMNe1WED4'
    contex = { 'list':list1,
              'api_key': api_key,
              'lat': lat,
              'long': '-48.06575099999998',
              'ult':ult,
              'listO':listO,

              }
    #return JsonResponse(list)
    return render(request,"index.html", contex)

