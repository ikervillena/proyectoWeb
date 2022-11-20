from django.contrib import admin
from .models import Ordenador, Telefono, Audio, Cliente

# Register your models here.
admin.site.register(Ordenador)
admin.site.register(Telefono)
admin.site.register(Audio)
admin.site.register(Cliente)
