from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add/', views.agregar_vehiculo, name='add'),
    path('vehiculo/listar', views.listar_vehiculos, name='listar'),
]
