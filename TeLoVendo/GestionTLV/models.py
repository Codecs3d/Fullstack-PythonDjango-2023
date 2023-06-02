from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)  
    titulo = models.CharField(max_length=50) #Pendiente EnProceso EnCamino Entregado
    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class FormaPago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    orden=models.CharField(max_length=50)
    fecha = models.DateField(default = timezone.now)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
    id_pago = models.ForeignKey(FormaPago, on_delete=models.DO_NOTHING)
    id_cliente = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    total = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)

class InfoCliente(models.Model):
    id_info = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=9)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    id_cliente = models.ForeignKey(User, on_delete=models.DO_NOTHING)