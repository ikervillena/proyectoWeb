from django.shortcuts import render
from .forms import UsuarioForm
from .forms import ClienteForm
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Producto, Ordenador, Audio, Telefono, Cliente
from django.shortcuts import get_object_or_404

# Create your views here.

def inicio(request):
    return render(request, 'Inicio.html')

def show_inicioSesion_form(request):
    form = UsuarioForm()
    return render(request, 'inicioSesion_form.html', {'form': form})

# Comprueba el inicio de sesión y redirige a página de detalle del usuario
def post_inicioSesion_form(request):
    form = UsuarioForm(request.POST)
    if form.is_valid():
        usuario_inicioSesion = form.cleaned_data['usuario']
        contrasenya_inicioSesion = form.cleaned_data['contrasenya']
        # Si el cliente no existe, se mantiene la página de inicio de sesión
        try:
            cliente = Cliente.objects.get(usuario=usuario_inicioSesion)
        except Cliente.DoesNotExist:
            form = UsuarioForm()
            return render(request, 'inicioSesion_form.html', {'form': form})
           
        if cliente.contrasenya==contrasenya_inicioSesion:
            return render(request, 'DetalleCliente.html', {'cliente': cliente, })

def show_registro_form(request):
    form = ClienteForm()
    return render(request, 'Registro_form.html', {'form': form})

# Recibe los datos introducidos por el usuario, almacena en la BBDD y los muestra en la página de detalle del usuario
def post_registro_form(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        nombre_registro = form.cleaned_data['nombre']
        usuario_registro = form.cleaned_data['usuario']
        contrasenya_registro = form.cleaned_data['contrasenya']
        email_registro = form.cleaned_data['email']

        #Si el nombre de usuario ya existe, no registrar cliente. Si no existe, registrar cliente.
        try:
            cliente = Cliente.objects.get(usuario=usuario_registro)
            form = ClienteForm()
            return render(request, 'Registro_form.html', {'form': form})
        except Cliente.DoesNotExist:
            cliente = Cliente(nombre=nombre_registro, usuario=usuario_registro, contrasenya=contrasenya_registro, email=email_registro)
            cliente.save()
            return render(request, 'DetalleCliente.html', {'cliente': cliente})

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

def detalleOrdenador(request, ordenador_id):
    try:
        ordenador = Ordenador.objects.get(pk=ordenador_id)
        context = {'ordenador': ordenador}
        return render(request, 'DetalleOrdenador.html', context)
    except Ordenador.DoesNotExist:
        return render(request, 'ErrorProducto.html')
    

def detalleTelefono(request, telefono_id):
    telefono = get_object_or_404(Telefono, pk=telefono_id)
    context = {'telefono': telefono}
    return render(request, 'DetalleTelefono.html', context)

def detalleAudio(request, audio_id):
    audio = get_object_or_404(Audio, pk=audio_id)
    context = {'audio': audio}
    return render(request, 'DetalleAudio.html', context)
