from django.contrib import admin
from pedidos.models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("crear_en", "actualizar", "estado")
