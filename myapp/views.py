from django.shortcuts import render
from .forms import UsuarioForm
from .forms import ClienteForm
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Producto, Ordenador, Audio, Telefono, Cliente
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

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
        
        #Comprueba contrasenya
        if cliente.contrasenya==contrasenya_inicioSesion:
            return render(request, 'DetalleCliente.html', {'cliente': cliente})
        else:
            form = UsuarioForm()
            return render(request, 'inicioSesion_form.html', {'form': form})

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

class OrdenadorListView(ListView):
    model = Ordenador
    template_name = 'ordenadores.html'
    queryset = Ordenador.objects.order_by('precio')
    context_object_name = 'lista_ordenadores'

    def get_context_data(self, **kwargs):
        context = super(OrdenadorListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = _('Ordenadores')
        return context

class AudioListView(ListView):
    model = Audio
    template_name = 'audios.html'
    queryset = Audio.objects.order_by('precio')
    context_object_name = 'lista_audios'

    def get_context_data(self, **kwargs):
        context = super(AudioListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = _('Audios')
        return context

class TelefonoListView(ListView):
    model = Telefono
    template_name = 'telefonos.html'
    queryset = Telefono.objects.order_by('precio')
    context_object_name = 'lista_telefonos'

    def get_context_data(self, **kwargs):
        context = super(TelefonoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = _('Teléfonos')
        return context


class OrdenadorDetailView(DetailView):
    model = Ordenador
    template_name = 'DetalleOrdenador.html'


class AudioDetailView(DetailView):
    model = Audio
    template_name = 'DetalleAudio.html'

class TelefonoDetailView(DetailView):
    model = Telefono
    template_name = 'DetalleTelefono.html'

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
