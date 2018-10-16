from rest_framework import routers
from .api.viewsets import DadosViewSet,DispositivoViewSet
from . import views
router = routers.DefaultRouter()
router.register(r'dados', DadosViewSet)
router.register(r'dispositivos', DispositivoViewSet)
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('add/', views.add),

    path('dadoslist/', views.DadosList.as_view()),
    path('dadosdetail/<int:pk>/', views.DadosDetail.as_view()),

    path('ds/', views.snippet_list),
    path('ds/<int:pk>/', views.snippet_detail),


    path('index/', views.teste),
    path('', views.teste),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
