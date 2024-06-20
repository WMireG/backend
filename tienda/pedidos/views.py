from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def vista_pedidos(request):
    return HttpResponse("Hola!, esta es la vista del pedido")

class Home(TemplateView):
    template_name = "pedidos.html"