from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre_artista = models.CharField(max_length=255, verbose_name='Nombre del Artista')
    nombre_disco = models.CharField(max_length=255, default='Sin Nombre', verbose_name='Nombre del Disco')
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, related_name="productos", on_delete=models.CASCADE)
    imagen_tapa = models.ImageField(upload_to='img/', blank=True, null=True) #Campo para la imagen del disco
        
    def __str__(self):
        return f'{self.nombre_artista} - {self.nombre_disco}'