from rest_framework import routers
from .api.viewsets import DadosViewSet,DispositivoViewSet
from . import views
router = routers.DefaultRouter()
router.register(r'dados', DadosViewSet)
router.register(r'dispositivos', DispositivoViewSet)
from django.urls import path,include

urlpatterns = [
    path('index/', views.teste),
    path('', views.teste),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]