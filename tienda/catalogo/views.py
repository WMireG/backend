from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Producto

class Home(TemplateView):
    template_name = "catalogo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()  # Obtener todos los productos del catálogo
        return context

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    context = {
        'producto': producto
    }
    return render(request, 'detalle_producto.html', context)