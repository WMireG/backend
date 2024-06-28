from django.views.generic import TemplateView
from django.db.models import Q
from catalogo.models import Producto

class TiendaView(TemplateView):
    template_name = 'index.html'
    success_url = 'index'

class BuscarView(TemplateView):
    template_name = 'buscar_view.html'  # Ajusta el nombre de tu plantilla

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')  # Obtiene el término de búsqueda desde la URL
        if query:
            # Realiza la búsqueda en tu modelo de Producto
            resultados = Producto.objects.filter(
                Q(nombre_artista__icontains=query) |  # Busca por nombre del artista
                Q(nombre_disco__icontains=query)  # Busca por nombre del disco
            )
        else:
            resultados = Producto.objects.none()  # Si no hay consulta, no muestra ningún resultado

        context['resultados'] = resultados
        context['query'] = query
        return context