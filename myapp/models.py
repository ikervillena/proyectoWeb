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
    
    def __str__(self):
        return self.nombre

class Telefono(Producto):
    #Atributos

    def __str__(self):
        return self.nombre

class Audio(Producto):
    #Atributos

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    usuario = models.CharField(max_length=60)
    contrasenya = models.CharField(max_length=60)
    email = models.EmailField()
    productos_guardados = models.ManyToManyField(Producto)
