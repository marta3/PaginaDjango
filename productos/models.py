from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Perfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usuario=models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono=models.CharField(max_length=20)


class Productos(models.Model):
    postre="Postre"
    comidas="Comidas"
    bebidas="Bebidas"
    t_productos=((postre,"Postre"),(comidas,"Comidas"),(bebidas,"Bebidas"))
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=150)
    precio=models.FloatField()
    foto=models.ImageField(upload_to="fotos/",default='fotos/fotico.png')
    categoria=models.CharField(max_length=10,choices=t_productos, default=comidas)
    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    nom_usu=models.ForeignKey(User,on_delete=models.CASCADE)
    id_prod=models.ManyToManyField(Productos)


class Carrito(models.Model):
    nom_usu=models.ForeignKeyuser = models.ForeignKey(User,on_delete=models.CASCADE)
    id_prod=models.ManyToManyField(Productos)
