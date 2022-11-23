from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.

class Producto(PolymorphicModel):
    nombre = models.CharField(max_length=40, default='producto')
    descripcion = models.TextField(default = 'descripcion')
    precio = models.FloatField(default = 0)
    imagen = models.ImageField(default = None)

    def __str__(self):
        return self.nombre

class Ordenador(Producto):
    #Atributos
    procesador = models.IntegerField(default=0)
    microfono = models.CharField(max_length=10, default= 'microfono')
    memoria = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre

class Telefono(Producto):
    #Atributos
    acabado = models.CharField(default="", max_length=15)
    capacidad = models.IntegerField(default=0)
    pantalla = models.FloatField(default=0)

    def __str__(self):
        return self.nombre

class Audio(Producto):
    #Atributos
    numeroWoofer = models.IntegerField(default = 1)
    diametroWoofer = models.FloatField(default=16)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    usuario = models.CharField(max_length=60)
    contrasenya = models.CharField(max_length=60)
    email = models.EmailField()
    productos_guardados = models.ManyToManyField(Producto, blank=True)

    def __str__(self):
        return self.nombre
