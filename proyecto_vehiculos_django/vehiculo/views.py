from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request, 'index.html')

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()

    # Asignar condición de precio
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = "Bajo"
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.condicion_precio = "Medio"
        else:
            vehiculo.condicion_precio = "Alto"

    return render(request, 'vehiculo/listar.html', {'vehiculos': vehiculos})

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el vehículo en la base de datos
            return redirect('vehiculo_list')  # Cambia por el nombre de la vista donde se listan los vehículos
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add.html', {'form': form})
