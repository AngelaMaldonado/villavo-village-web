from django.shortcuts import render, redirect
from .forms import ContratoHospedajeForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError
from .serializers import ContratoHospedajeSerializer


def home(request) :
    return render(request, 'index.html')
@csrf_exempt
def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoHospedajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contrato_exito')  # Puedes redirigir a una página de éxito
    else:
        form = ContratoHospedajeForm()

    return render(request, 'crear_contrato.html', {'form': form})

def contrato_exito(request):
    return HttpResponse("¡El contrato ha sido registrado con éxito!")

@api_view(['POST'])
def api_crear_contrato(request):
    if request.method == 'POST':
        serializer = ContratoHospedajeSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'error': 'El número de reserva ya existe.'}, status=status.HTTP_400_BAD_REQUEST)

def proyecto_1(request):
    return render(request, 'santorini.html')

def contacto(request):
    return render(request, 'contactanos.html')