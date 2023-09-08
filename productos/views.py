from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto


def index( request ):
    return render(request, 'index.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

#def registrar_producto(request):
#    if request.method == 'POST':
#        regis= ProductoForm(request.POST)
#        if regis.is_valid():
#            regis.save()
#            return redirect('listar_productos')
#    else:
#        regis = ProductoForm()
#    return render(request, 'productos/registrar_producto.html', {'regis': regis})
from django.shortcuts import render, redirect
from .forms import ProductoForm

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()

    return render(request, 'tipos_productos/registrar_producto.html', {'form': form})
