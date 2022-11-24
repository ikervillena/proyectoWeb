from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicioSesion/', views.show_inicioSesion_form, name='inicioSesion_form'),
    path('inicioSesion/', views.post_inicioSesion_form, name='post_inicioSesion_form'),
    path('registro/', views.show_registro_form, name='registro_form'),
    path('registrado/', views.post_registro_form, name="post_registro_form"),
    path('ordenadores/', views.ordenadores, name="ordenadores"),
    path('audios/', views.audios, name="audios"),
    path('telefonos/', views.telefonos, name="telefonos"),
    path('inicio/', views.inicio, name="inicio"),
    path('ordenadores/<int:ordenador_id>', views.detalleOrdenador, name='detalle_ordenador'),
    path('telefonos/<int:telefono_id>', views.detalleTelefono, name='detalle_telefono'),
    path('audios/<int:audio_id>', views.detalleAudio, name='detalle_audio'),
]