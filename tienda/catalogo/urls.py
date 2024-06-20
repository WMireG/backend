from django.urls import path
from catalogo.views import Home, detalle_producto


urlpatterns = [
    path('', Home.as_view(), name='catalogo'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto')
]