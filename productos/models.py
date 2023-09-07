from django.db import models
from tipos_productos.models import TipoProducto

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo_barras = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_caducidad = models.DateField()
    cantidad_inventario = models.PositiveIntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
