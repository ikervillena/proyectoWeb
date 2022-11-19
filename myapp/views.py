from django.shortcuts import render
from .forms import UsuarioForm

# Create your views here.

def show_form(request):
    return render(request, 'Inicio-sesión.html')

# def post_form(request):
#     usuario = request.POST("username")

def show_UsuarioForm(request):
    form = UsuarioForm
    return render(request, 'Inicio-sesión.html', {'form':form})