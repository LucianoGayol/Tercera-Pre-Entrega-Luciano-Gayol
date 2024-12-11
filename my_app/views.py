from django.shortcuts import render, redirect

from my_app.models import Cliente
from .forms import ClienteForm, ProductoForm, CompraForm

def inicio(request):
    return render(request, 'my_app/inicio.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'my_app/crear_cliente.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm()
    return render(request, 'my_app/crear_producto.html', {'form': form})

def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CompraForm()
    return render(request, 'my_app/crear_compra.html', {'form': form})


def buscar_cliente(request):
    resultados = []
    query = request.GET.get('q', '')
    if query:
        resultados = Cliente.objects.filter(nombre__icontains=query)
    return render(request, 'my_app/buscar_cliente.html', {'resultados': resultados, 'query': query})
