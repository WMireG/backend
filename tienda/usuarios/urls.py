from django.urls import path
from usuarios.views import Home

urlpatterns = [
    path('', Home.as_view(), name='usuarios'),
]