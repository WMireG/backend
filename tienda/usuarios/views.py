from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from autenticacion.forms import RegistrationForm


class Home(TemplateView):
    template_name = "usuarios.html"

class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_invalid(self,form):
        messages.error(
            self.request, "Datos incorrectos, por favor intentalo de nuevo"
        )
        return super().form_invalid(form)
  
class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registro.html"

    def form_valid(self, form):
        # Procesar el formulario si es válido
        user = form.save(commit=False)
        # Podemos hacer algo
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Agregar mensajes de error a la lista de mensajes
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)
class LogoutConfirmationView(LoginView):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "¡Has cerrado sesión correctamente!")
        return redirect('catalogo')  # Reemplaza con la URL a la que quieres redirigir