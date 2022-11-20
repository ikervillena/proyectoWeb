from django.shortcuts import get_object_or_404, render
from .forms import ClienteForm
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Producto, Ordenador, Audio, Telefono, Cliente

# Create your views here.

def show_registro_form(request):
    form = ClienteForm()
    return render(request, 'Registro_form.html', {'form': form})

def post_registro_form(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        nombre_registro = form.cleaned_data['nombre']
        usuario_registro = form.cleaned_data['usuario']
        contrasenya_registro = form.cleaned_data['contrasenya']
        email_registro = form.cleaned_data['email']
        cliente = Cliente(nombre=nombre_registro, usuario=usuario_registro, contrasenya=contrasenya_registro, email=email_registro)
        cliente.save()
        return render(request, 'DetalleCliente.html', {'cliente': cliente})

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

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    context = {'producto': producto}
    return render(request, 'VistaDetalle.html', context)

#def detalle_telefono(request, telefono_id):
    #telefono = get_object_or_404(Telefono,pk=telefono_id)
    #context = {'telefono': telefono}
    #return render(request, 'VistaDetalle.html', context)

#def detalle_ordenador(request, ordenador_id):
    #ordenador = get_object_or_404(Ordenador,pk=ordenador_id)
    #context = {'ordenador': ordenador}
    #return render(request, 'VistaDetalle.html', context)

#def detalle_audio(request, audio_id):
    #audio = get_object_or_404(Telefono,pk=audio_id)
    #context = {'audio': audio}
    #return render(request, 'VistaDetalle.html', context)