from django.db import models

# Create your models here.
class ContratoHospedaje(models.Model):
    reserva_no = models.CharField(max_length=100, unique=True)
    plataforma = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    nombre_huesped = models.CharField(max_length=100)
    apellidos_huesped = models.CharField(max_length=100)
    numero_identidad = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    ciudad_residencia = models.CharField(max_length=100)
    motivo_viaje = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    ocupacion = models.CharField(max_length=100)
    medio_pago = models.CharField(max_length=50)
    duracion = models.IntegerField(help_text="Duración en días")

    def __str__(self):
        return f"{self.nombre_huesped} {self.apellidos_huesped} - Reserva No. {self.reserva_no}"
