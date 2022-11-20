from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.show_registro_form, name='registro_form'),
    path('registrado/', views.post_registro_form, name="post_registro_form"),
    path('tipoProducto/', views.tipo_producto, name="tipo_producto")
]