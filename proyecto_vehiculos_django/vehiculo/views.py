from django.shortcuts import render, redirect
from .forms import VehiculoForm

def index(request):
    return render(request, 'index.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el vehículo en la base de datos
            return redirect('vehiculo_list')  # Cambia por el nombre de la vista donde se listan los vehículos
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo_add.html', {'form': form})
