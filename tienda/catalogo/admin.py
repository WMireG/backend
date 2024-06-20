from django.contrib import admin
from catalogo.models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre_artista", "nombre_disco", "descripcion", "precio", "stock")