from django.views.generic import TemplateView
# # Create your views here.
# def vista_pedidos(request):
#     return HttpResponse("Hola!, esta es la vista principal?")

# class Home(TemplateView):
#     template_name = "index.html"

class TiendaView(TemplateView):
    template_name = 'index.html'
    success_url = 'index'

    # def form_valid(self, form):
    #     # Procesar el formulario si es válido
    #     user = form.save(commit=False)
    #     user.save()
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     # Agregar mensajes de error a la lista de mensajes
    #     for field, errors in form.errors.items():
    #         for error in errors:
    #             messages.error(self.request, f"{field}: {error}")
    #     return super().form_invalid(form)

from django.shortcuts import render
from django.db.models import Q
from catalogo.models import Producto

# def buscar_view(request):
#     query = request.GET.get('q')  # Obtiene el término de búsqueda desde la URL

#     if query:
#         # Realiza la búsqueda en tu modelo de Producto (o cualquier otro modelo que quieras buscar)
#         resultados = Producto.objects.filter(
#             Q(nombre_artista__icontains=query) |  # Busca por nombre del artista (insensible a mayúsculas y minúsculas)
#             Q(nombre_disco__icontains=query)  # Busca por nombre del disco (insensible a mayúsculas y minúsculas)
#         )
#     else:
#         resultados = Producto.objects.none()  # Si no hay consulta, no muestra ningún resultado

#     context = {
#         'resultados': resultados,
#         'query': query,
#     }

#     return render(request, 'buscar_view.html', context)


from django.db.models import Q
from catalogo.models import Producto

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