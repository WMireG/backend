from django.db import models, transaction
from usuarios.models import CustomUser
from catalogo.models import Producto
from django.db.models import F, Sum

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
    
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Define el campo total
    
    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    @transaction.atomic
    def actualizar_total(self):
        total_pedido = self.orderitem_set.aggregate(total=Sum(F('producto__precio') * F('cantidad'), output_field=models.FloatField()))['total'] or 0
        self.total = total_pedido
        Pedido.objects.filter(id=self.id).update(total=self.total)  # Actualiza el total sin llamar a save() recursivamente
    
    def marcar_como_entregado(self):
        self.estado = "Entregado"
        self.save(update_fields=['estado'])
    
    @transaction.atomic
    def eliminar_pedido(self):
        self.delete()
    
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