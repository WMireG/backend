from django.urls import path
from carrito.views import Home
from . import views


urlpatterns = [
    path('', Home.as_view(), name='carrito'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('limpiar/', views.limpiar_carro, name='limpiar_carro'),    
]