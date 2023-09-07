
from django.shortcuts import render, redirect
from .forms import TipoProductoForm
from .models import TipoProducto

def listar_tipos_productos(request):
    tipos_productos = TipoProducto.objects.all()
    return render(request, 'tipos_productos/listar_tipos_productos.html', {'tipos_productos': tipos_productos})

def registrar_tipo_producto(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_productos')
    else:
        form = TipoProductoForm()
    return render(request, 'tipos_productos/registrar_tipo_producto.html', {'form': form})
