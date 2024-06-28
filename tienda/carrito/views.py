from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from catalogo.models import Producto
from carrito.carro import Carro

class Home(TemplateView):
    template_name = "carrito.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carro = Carro(self.request)
        productos_en_carro = []
        for item in carro.carro.values():
            producto = Producto.objects.get(id=item['producto_id'])  # Ajusta según cómo guardas los productos en el carro
            producto.cantidad = item['cantidad']
            producto.subtotal = item['precio'] * item['cantidad']  # Calcula el subtotal según tu lógica
            # Agregar la imagen al producto si está disponible
            producto.imagen_tapa = producto.imagen_tapa.url if producto.imagen_tapa else None
            productos_en_carro.append(producto)
        context['productos'] = productos_en_carro
        context['total'] = carro.obtener_total()
        return context
    
@method_decorator(login_required, name='dispatch')
class OperacionesCarro(View):
    def post(self, request, action, producto_id):
        carro = Carro(request)
        producto = Producto.objects.get(id=producto_id)

        if action == 'agregar':
            carro.agregar(producto)
            next_url = 'catalogo'
        elif action == 'eliminar':
            carro.eliminar(producto)
            next_url = 'carrito'
        elif action == 'restar':
            carro.restar_producto(producto)
            next_url = 'carrito'
        elif action == 'limpiar':
            carro.limpiar_carro(producto)
            next_url = 'catalogo'
        else:
            # Manejar caso no definido
            next_url = 'catalogo'

        return redirect(next_url)