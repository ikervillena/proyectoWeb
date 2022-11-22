from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.show_registro_form, name='registro_form'),
    path('registrar/', views.registrar, name="registrar"),
    path('ordenadores/', views.ordenadores, name="ordenadores"),
    path('audios/', views.audios, name="audios"),
    path('telefonos/', views.telefonos, name="telefonos"),
    path('inicio/', views.inicio, name="inicio"),
    path('view/<int:producto_id>', views.detalle, name='vista_detalle')
]