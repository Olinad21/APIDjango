from django.db import models

from django.db import models


class Dados(models.Model):
    leituraUV = models.IntegerField()
    data = models.DateTimeField()
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE)

    def __str__(self):
        return "Índice UV: %d" % (self.leituraUV)

class Dispositivo(models.Model):
    nome = models.CharField(max_length=190)
    longitude = models.FloatField(null=True,blank=True,default=None)
    latitude = models.FloatField(null=True,blank=True,default=None)

    def __str__(self):
        return "Dispositivo: %s" % (self.nome)
