from django.contrib import admin
from .models import Producto, Ordenador, Telefono, Audio, Cliente

# Register your models here.
admin.site.register(Telefono)
admin.site.register(Audio)
admin.site.register(Cliente)
admin.site.register(Ordenador)
