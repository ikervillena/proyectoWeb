from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicioSesion/', views.show_inicioSesion_form, name='inicioSesion_form'),
    path('iniciado/', views.post_inicioSesion_form, name='post_inicioSesion_form'),
    path('registro/', views.show_registro_form, name='registro_form'),
    path('registrado/', views.post_registro_form, name="post_registro_form"),
    path('ordenadores/', views.OrdenadorListView.as_view(), name="ordenadores"),
    path('audios/', views.AudioListView.as_view(), name="audios"),
    path('telefonos/', views.TelefonoListView.as_view(), name="telefonos"),
    path('ordenadores/<int:pk>', views.OrdenadorDetailView.as_view(), name='detalle_ordenador'),
    path('telefonos/<int:pk>', views.TelefonoDetailView.as_view(), name='detalle_telefono'),
    path('audios/<int:pk>', views.AudioDetailView.as_view(), name='detalle_audio'),
    path('i18n/', views.set_language, name='set_language'),
]