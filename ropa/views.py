from django.shortcuts import render, redirect
from .forms import RegistroForm, PrendaForm
from .models import Prenda

def inicio(request):
    prendas = Prenda.objects.all()
    return render(request, 'ropa/inicio.html', {'prendas': prendas})

def agregar_prenda(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PrendaForm()
    return render(request, 'ropa/agregar_prenda.html', {'form': form})

def buscar_prenda(request):
    query = request.GET.get('q', '')
    resultados = Prenda.objects.filter(nombre__icontains=query)
    return render(request, 'ropa/buscar_prenda.html', {'resultados': resultados, 'query': query})

def acerca_de_mi(request):
    return render(request, 'ropa/acerca_de_mi.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'ropa/registro.html', {'form': form})

def lista_productos(request):
    prendas = Prenda.objects.all()
    return render(request, 'ropa/lista_productos.html', {'prendas': prendas})
