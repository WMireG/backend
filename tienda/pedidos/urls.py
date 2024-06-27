from django.urls import path
from usuarios.views import CustomLoginView, RegistrationView, LogoutConfirmationView
from pedidos.views import HomeView, ProcesarPedidoView, ListaPedidosView, MarcarComoEntregadoView

urlpatterns = [
    path('', HomeView.as_view(), name="pedidos"),
    path('procesar_pedido/', ProcesarPedidoView.as_view(), name='procesar_pedido'),
    path('lista_pedidos/', ListaPedidosView.as_view(), name='lista_pedidos'),
    path('pedidos/marcar_entregado/<int:pedido_id>/', MarcarComoEntregadoView.as_view(), name='marcar_entregado'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("registro/", RegistrationView.as_view(), name="registro"),
    path("confirm_logout/", LogoutConfirmationView.as_view(), name="confirm_logout"),
]