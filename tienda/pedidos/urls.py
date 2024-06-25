from django.urls import path
from pedidos.views import Home, procesar_pedido


urlpatterns = [
    path('', Home.as_view(), name='pedidos'),
    path('procesar_pedido/', procesar_pedido, name='procesar_pedido')
]