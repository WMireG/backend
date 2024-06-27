from django.urls import path
from usuarios.views import CustomLoginView, RegistrationView, LogoutConfirmationView
from pedidos.views import HomeView, ProcesarPedidoView, ListaPedidosView, BorrarPedidos

urlpatterns = [
    path('', HomeView.as_view(), name="pedidos"),
    path('procesar_pedido/', ProcesarPedidoView.as_view(), name='procesar_pedido'),
    path('lista_pedidos/', ListaPedidosView.as_view(), name='lista_pedidos'),
    path('borrar_pedidos/', BorrarPedidos.as_view(), name='borrar_pedidos'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("registro/", RegistrationView.as_view(), name="registro"),
    path("confirm_logout/", LogoutConfirmationView.as_view(), name="confirm_logout"),
]