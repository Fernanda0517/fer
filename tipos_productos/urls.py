from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_tipos_productos, name='listar_productos'),
    ]
