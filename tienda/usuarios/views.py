from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
def vista_usuarios(request):
    return HttpResponse("Hola!, esta es la vista del usuarios")

class Home(TemplateView):
    template_name = "usuarios.html"

