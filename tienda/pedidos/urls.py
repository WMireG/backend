from django.urls import path
from pedidos.views import Home

urlpatterns = [
    path('', Home.as_view(), name='pedidos'),
]