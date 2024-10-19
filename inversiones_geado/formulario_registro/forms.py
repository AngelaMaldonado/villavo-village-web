from django import forms
from .models import ContratoHospedaje

class ContratoHospedajeForm(forms.ModelForm):
    class Meta:
        model = ContratoHospedaje
        fields = ['reserva_no', 'plataforma', 'direccion', 'nombre_huesped', 'apellidos_huesped',
                  'numero_identidad', 'nacionalidad', 'ciudad_residencia', 'motivo_viaje',
                  'correo_electronico', 'ocupacion', 'medio_pago', 'duracion', 'telefono']
