from django.views.generic import TemplateView
from catalogo.models import Producto
from django.views.generic import DetailView

class Home(TemplateView):
    template_name = "catalogo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()  # Obtener todos los productos del catálogo
        return context

class DetalleProductoView(DetailView):
    model = Producto
    template_name = "detalle_producto.html"
    context_object_name = 'producto'  
    pk_url_kwarg = 'producto_id'