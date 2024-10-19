from django.urls import path
from . import views

urlpatterns = [
    path('crear-contrato/', views.crear_contrato, name='crear_contrato'),
    path('contrato-exito/', views.contrato_exito, name='contrato_exito'),
    path('api/crear-contrato/', views.api_crear_contrato, name='api_crear_contrato')
]
