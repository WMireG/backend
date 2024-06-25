from django.db import models
from usuarios.models import CustomUser
from catalogo.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.
class Pedido(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    crear_en = models.DateTimeField(auto_now_add=True)
    actualizar = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=50, choices=[
        ("Pendiente", "Pendiente"),
        ("EnProceso", "EnProceso"),
        ("Enviado", "Enviado"),
        ("Entregado", "Entregado"),
        ("Cancelado", "Cancelado")
    ], default="Pendiente")
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
        total_pedido = 0
        order_items = self.orderitem_set.all()
        for item in order_items:
            total_pedido += item.producto.precio * item.cantidad
        return total_pedido
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class OrderItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    crear_en = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre_disco}"

    class Meta:
        db_table = 'orden_de_compra'
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Ordenes de Compra'
        ordering = ['id']