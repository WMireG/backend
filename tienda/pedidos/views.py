from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, OrderItem
from carrito.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from catalogo.models import Producto


# class Home(LoginRequiredMixin, TemplateView):
#     template_name = "pedidos.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Obtener todos los pedidos del usuario actual
#         user = self.request.user
#         pedidos = Pedido.objects.filter(user=user)
#         context['pedidos'] = pedidos
#         return context

# @login_required(login_url = '/usuarios/login')
# def procesar_pedido(request):
#     pedido = Pedido.objects.create(user=request.user)
#     carro = Carro(request)
#     lineas_pedidos = list()
#     for key, value in carro.carro.items():
#         producto = Producto.objects.get(id=key)#asegura obtener el producto correcto
#         lineas_pedidos.append(OrderItem(
#             producto = key,
#             cantidad = value['cantidad'],
#             user = request.user,
#             pedido = pedido
#         ))
#         lineas_pedidos.append(lineas_pedidos)
    
#     #Esto metodo hace muchos "INSERT_INTO" como si los procesaras en lote.
#     #Y en teoria, guarda los items del pedido en la BD.
#     OrderItem.objects.bulk_create(lineas_pedidos)
    
#     #Limpia el carrito despues de procesar el pedido
#     carro.limpiar_carro()
    
# @login_required(login_url='usuarios/login')
# def lista_pedidos(request):
#     pedidos = Pedido.objects.filter(user=request.user)
#     return render(request, 'pedidos.html', {'pedidos': pedidos})
    
# # # # # #Envia mails cuando el pedido fue creado
# #     enviar_mail(
# #         pedido = pedido,
# #         lineas_pedidos = lineas_pedidos,
# #         username = request.user.username,
# #         emailusuario = request.user.email
# #     )
    
# #     messages.success(request, "El pedido se ha creado correctamente")
    
# #     return redirect("catalogo")


# # def enviar_mail(**kwargs):
# #     asunto = 'Gracias por el pedido'
# #     mensaje = render_to_string("emails/pedido.html", {
# #         "pedido": kwargs.get("pedido"),
# #         "lineas_pedidos": kwargs.get("lineas_pedidos"),
# #         "username": kwargs.get("username")
# #     })
    
# #     mensaje_texto = strip_tags(mensaje)
# #     from_email="walteriorlz@gmail.com" #puro chequeo
# #     to = kwargs.get("emailusuario")
    
# #     send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)


class Home(LoginRequiredMixin, TemplateView):
    template_name = "pedidos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener todos los pedidos del usuario actual
        user = self.request.user
        pedidos = Pedido.objects.filter(user=user)
        context['pedidos'] = pedidos
        return context

@login_required(login_url='/usuarios/login')
def procesar_pedido(request):
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
    
    # Redirige a la página de pedidos o a donde sea necesario
    return redirect('pedidos')

@login_required(login_url='/usuarios/login')
def lista_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user)
    return render(request, 'pedidos.html', {'pedidos': pedidos})