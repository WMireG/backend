from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .carro import Carro
from catalogo.models import Producto
from django.contrib.auth.decorators import login_required


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
    
@login_required
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("catalogo")

@login_required
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("carrito")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("catalogo")