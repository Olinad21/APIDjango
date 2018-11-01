from django.shortcuts import render
from .models import Dispositivo,Dados
from .serializers import DadosSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from datetime import datetime, timedelta, time
from django.utils import timezone

def list(request):
    today = timezone.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    listO = Dados.objects.select_related('dispositivo')
    loc = Dispositivo.objects.get(pk=1)
    list = Dados.objects.all().filter(dispositivo=1).filter(data__lte=today_end, data__gte=today_start)
    ult = Dados.objects.latest('data')
    listDisp = Dispositivo.objects.all()

    api_key = 'AIzaSyC-gwBjleF-ixYwe5NhiF6TMVIMNe1WED4'
    contex = { 'list':list,
              'api_key': api_key,
              'lat': loc,
              'long': loc,
              'ult':ult,
              'listO':listO,
              'listDisp':listDisp,

              }
    #return JsonResponse(list)
    return render(request,"index.html", contex)

def add(request):
    if (request.method=='POST'):
        request.create

    listDisp = Dispositivo.objects.all()
    contex = {'listDisp': listDisp,}
    return render(request,"add.html",contex)







# class DadosList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         dados = Dados.objects.all()
#         serializer = DadosSerializer(dados, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = DadosSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class DadosDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Dados.objects.get(pk=pk)
#         except Dados.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         dados = self.get_object(pk)
#         serializer = DadosSerializer(dados)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = DadosSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET', 'POST'])
# def dados(request,format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         dados = Dados.objects.all()
#         serializer = DadosSerializer(dados, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = DadosSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def dados(request, pk,format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         dados = Dados.objects.get(pk=pk)
#     except Dados.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = DadosSerializer(dados)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = DadosSerializer(dados, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         dados.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#





