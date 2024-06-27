from django.urls import path
from catalogo.views import Home, DetalleProductoView


urlpatterns = [
    path('', Home.as_view(), name='catalogo'),
    path('producto/<int:producto_id>/', DetalleProductoView.as_view(), name='detalle_producto')
]