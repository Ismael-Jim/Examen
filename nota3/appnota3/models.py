from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' -- ' + self.usuario.username

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Boleta {self.id} - {self.tienda.nombre}"
