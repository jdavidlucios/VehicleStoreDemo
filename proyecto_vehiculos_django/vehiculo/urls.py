from django.urls import path
from . import views
from .views import agregar_vehiculo

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo_add', agregar_vehiculo, name='vehiculo/add'),
    path('vehiculo_list', agregar_vehiculo, name='vehiculo/list'),
]
