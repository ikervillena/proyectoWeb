from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    precio = models.FloatField()
    imagen = models.ImageField()

    class Meta:
        abstract = True

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
    fecha_nacimiento = models.DateField()
    productos_guardados = models.ManyToManyField(Producto)