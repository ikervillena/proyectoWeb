from django.shortcuts import render
from .forms import ClienteForm

# Create your views here.

def show_registro_form(request):
    form = ClienteForm()
    return render(request, 'Registro_form.html', {'form': form})

def registrar(request):
    return render(request, 'Registrarse.html')
