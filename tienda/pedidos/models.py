from django.db import models
from usuarios.models import CustomUser
from catalogo.models import Producto

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
        return f"Orden {self.id} by {self.user.username}"

class OrderItem(models.Model):
    Pedido = models.ForeignKey(Pedido, related_name="Items", on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.cantidad} de {self.Producto.name} en el pedido {self.Pedido.id}"
