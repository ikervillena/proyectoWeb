from django.urls import path
from . import views

urlpatterns = [
    path('inicioSesion/', views.show_form, name = 'inicioSesion'),
    # path('inicio/', views.post_form, name = 'inicio')
    path('usuario/', views.show_UsuarioForm, name = 'usuarioForm'),
    
]