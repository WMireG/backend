from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from pedidos.models import Pedido, OrderItem
from carrito.carro import Carro
from catalogo.models import Producto

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "pedidos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener todos los pedidos del usuario actual
        user = self.request.user
        pedidos = Pedido.objects.filter(user=user)
        context['pedidos'] = pedidos
        return context

class ProcesarPedidoView(LoginRequiredMixin, View):
    
    def post(self, request, *args, **kwargs):
        pedido = Pedido.objects.create(user=request.user)
        carro = Carro(request)
        lineas_pedidos = []
        for key, value in carro.carro.items():
            producto = Producto.objects.get(id=key)  # Asegura obtener el producto correcto
            item = OrderItem(
                producto=producto,
                cantidad=value['cantidad'],
                user=request.user,
                pedido=pedido
            )
            lineas_pedidos.append(item)
        
        # Guarda los items del pedido en la BD usando bulk_create
        OrderItem.objects.bulk_create(lineas_pedidos)
        
        # Limpia el carrito después de procesar el pedido
        carro.limpiar_carro()
        
        # Marca el pedido como entregado
        pedido.marcar_como_entregado()
        
        # Redirige a la página de pedidos o a donde sea necesario
        return redirect('pedidos')
    
class BorrarPedidos(View):
    def post(self, request, *args, **kwargs):
        Pedido.objects.all().delete()
        return redirect('catalogo')

class ListaPedidosView(LoginRequiredMixin, ListView):
    template_name = 'pedidos.html'
    model = Pedido
    context_object_name = 'pedidos'
    
    def get_queryset(self):
        return Pedido.objects.filter(user=self.request.user)