from rest_framework import serializers
from .models import ContratoHospedaje

class ContratoHospedajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratoHospedaje
        fields = '__all__'  # Incluye todos los campos del modelo
