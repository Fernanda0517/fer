from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('listar/', views.listar_productos, name='listar_productos'),
    path('registrar/', views.registrar_producto, name='registrar_producto'),
    #path('')
    #path('registrar/', RegistrarProductoView.as_view(), name='registrar_producto'),
]

