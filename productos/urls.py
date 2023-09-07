from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_productos, name='listar_productos'),
    path('registrar/', views.registrar_producto, name='registrar_producto'),
]
