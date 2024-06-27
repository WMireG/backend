from django.urls import path
from carrito.views import OperacionesCarro, Home

urlpatterns = [
    path('', Home.as_view(), name = 'carrito'),
    path('carro/agregar/<int:producto_id>/', OperacionesCarro.as_view(), {'action': 'agregar'}, name='agregar_producto'),
    path('carro/eliminar/<int:producto_id>/', OperacionesCarro.as_view(), {'action': 'eliminar'}, name='eliminar_producto'),
    path('carro/restar/<int:producto_id>/', OperacionesCarro.as_view(), {'action': 'restar'}, name='restar_producto'),
    path('carro/limpiar/', OperacionesCarro.as_view(), {'action': 'limpiar'}, name='limpiar_carro'),
]