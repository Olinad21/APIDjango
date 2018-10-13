from rest_framework import routers
from .api.viewsets import DadosViewSet,DispositivoViewSet

router = routers.DefaultRouter()
router.register(r'dados', DadosViewSet)
router.register(r'dispositivos', DispositivoViewSet)
from django.urls import path,include

urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]