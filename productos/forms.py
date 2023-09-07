from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo_barras', 'precio', 'fecha_caducidad', 'cantidad_inventario', 'tipo']

