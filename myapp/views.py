from django.shortcuts import render
from .forms import ClienteForm
from .models import Producto, Ordenador, Audio, Telefono

# Create your views here.

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
def lista_ordernadores(request):
    ordenadores = Ordenador.objects.order_by('precio')
    context = { 'lista_ordenadores' : ordenadores}
    return render (request, 'TipoProducto.html', context)

# Devuelve los datos de un audio por ID
def audio(request):
    audio = Audio.objects.get(pk = audio_id)
    return HttpResponse(audio)

# Devuelve la lista de audios
def lista_audios(request):
    audios = Audio.objects.order_by('precio')
    context = { 'lista_audios' : audios}
    return render (request, 'TipoProducto.html', context)

# Devuelve los datos de un telefono por ID
def telefono(request):
    telefono = Telefono.objects.get(pk = telefono_id)
    return HttpResponse(telefono)

# Devuelve la lista de telefonos
def lista_telefonos(request):
    telefonos = Telefono.objects.order_by('precio')
    context = { 'lista_telefonos' : telefonos}
    return render (request, 'TipoProducto.html', context)

def tipo_producto(request):
    ordenadores = Ordenador.objects.order_by('precio')
    audios = Audio.objects.order_by('precio')
    telefonos = Telefono.objects.order_by('precio')
    context = {'lista_ordenadores' : ordenadores, 'lista_audios' : audios, 'lista_telefonos' : telefonos}
    return render (request, 'tipoProducto.html', context)