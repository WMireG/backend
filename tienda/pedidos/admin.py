from django.contrib import admin
from pedidos.models import Pedido, OrderItem


admin.site.register(Pedido)
admin.site.register(OrderItem)
