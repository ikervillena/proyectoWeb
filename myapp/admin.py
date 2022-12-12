from django.contrib import admin
from .models import Ordenador, Telefono, Audio, Cliente

# Register your models here. PRIMERA ENTREGA
# admin.site.register(Ordenador)
# admin.site.register(Telefono)
# admin.site.register(Audio)
# admin.site.register(Cliente)


#PERSONALIZANDO APLICACIÓN DE ADMIN
admin.site.site_header = 'Admin Tienda IM Componentes'

#Agruparlo y ponerle titulos
class OrdenadorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos Generales', {'fields': ['nombre', 'descripcion', 'precio', 'imagen']}),
        ('Otros datos', {'fields': ['proces', 'sistemaDeAudio', 'memoria']}),
    ]

    list_display= ('nombre', 'descripcion', 'precio')
    search_fields=['descripcion', 'nombre']
    list_filter= ['precio']

admin.site.register(Ordenador, OrdenadorAdmin)

#Agruparlo y ponerle titulos
class TelefonoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos Generales', {'fields': ['nombre', 'descripcion', 'precio', 'imagen']}),
        ('Otros datos', {'fields': ['acabado', 'capacidad', 'pantalla']}),
    ]
    list_display= ('nombre', 'descripcion', 'precio')
    search_fields=['descripcion', 'nombre']
    list_filter= ['precio']

#Agruparlo y ponerle titulos
admin.site.register(Telefono, TelefonoAdmin)

class AudioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos Generales', {'fields': ['nombre', 'descripcion', 'precio', 'imagen']}),
        ('Otros datos', {'fields': ['numeroWoofer', 'diametroWoofer']}),
    ]
    list_display= ('nombre', 'descripcion', 'precio')
    search_fields=['descripcion', 'nombre']
    list_filter= ['precio']

admin.site.register(Audio, AudioAdmin)


#Agruparlo y ponerle titulos
class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos del Cliente', {'fields': ['nombre', 'usuario', 'contrasenya', 'email']}),
        ('Productos', {'fields': ['productos_guardados']}),
    ]

    list_display= ('nombre', 'usuario', 'email')
    search_fields=['usuario', 'nombre']
    list_filter= ['productos_guardados']

admin.site.register(Cliente, ClienteAdmin)