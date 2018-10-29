from django.db import models
from datetime import datetime

class Dados(models.Model):
    leituraUV = models.IntegerField()
    data = models.DateTimeField(default=datetime.now(),)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE)

    def __str__(self):
        return "%d" % (self.leituraUV)





class Dispositivo(models.Model):
    nome = models.CharField(max_length=190)
    longitude = models.FloatField(null=True,blank=True,default=None)
    latitude = models.FloatField(null=True,blank=True,default=None)

    def __str__(self):
        return (self.nome)
