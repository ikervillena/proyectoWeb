from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.show_registro_form, name='registro_form'),
    path('registrar/', views.registrar, name="registrar"),
    path('tipoProducto/', views.tipo_producto, name="tipo_producto")
]