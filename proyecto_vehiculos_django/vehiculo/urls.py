from django.urls import path
from . import views
from .views import agregar_vehiculo

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add/', agregar_vehiculo, name='vehiculo_add'),
]
