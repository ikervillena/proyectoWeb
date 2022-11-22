from django.shortcuts import render
from .forms import ClienteForm
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Producto, Ordenador, Audio, Telefono
from django.shortcuts import get_object_or_404

# Create your views here.

def inicio(request):
    return render(request, 'Inicio.html')

def show_registro_form(request):
    form = ClienteForm()
    return render(request, 'Registro_form.html', {'form': form})

def registrar(request):
    return render(request, 'Registrarse.html')

# Devuelve los datos de un ordenador por ID
def ordenador(request):
    ordenador = Ordenador.objects.get(pk = ordenador_id)
    return HttpResponse(ordenador)

# Devuelve la lista de ordenadores
def ordenadores(request):
    ordenadores = Ordenador.objects.order_by('precio')
    context = { 'lista_ordenadores' : ordenadores}
    return render (request, 'ordenadores.html', context)

# Devuelve los datos de un audio por ID
def audio(request):
    audio = Audio.objects.get(pk = audio_id)
    return HttpResponse(audio)

# Devuelve la lista de audios
def audios(request):
    audios = Audio.objects.order_by('precio')
    context = { 'lista_audios' : audios}
    return render (request, 'audios.html', context)

# Devuelve los datos de un telefono por ID
def telefono(request):
    telefono = Telefono.objects.get(pk = telefono_id)
    return HttpResponse(telefono)

# Devuelve la lista de telefonos
def telefonos(request):
    telefonos = Telefono.objects.order_by('precio')
    context = { 'lista_telefonos' : telefonos}
    return render (request, 'telefonos.html', context)

def tipo_producto(request):
    ordenadores = Ordenador.objects.order_by('precio')
    audios = Audio.objects.order_by('precio')
    telefonos = Telefono.objects.order_by('precio')
    context = {'lista_ordenadores' : ordenadores, 'lista_audios' : audios, 'lista_telefonos' : telefonos}
    return render (request, 'tipoProducto.html', context)

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk = producto_id)
    context = {'producto': producto}
    return render(request, 'VistaDetalle.html', context)
