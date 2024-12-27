from django.shortcuts import render, redirect, get_object_or_404

from my_app.models import Cliente
from .forms import ClienteForm, ProductoForm, CompraForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto


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

def listar_clientes(request):
    clientes = Cliente.objects.all() 
    return render(request, 'my_app/listar_clientes.html', {'clientes': clientes})

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'my_app/editar_cliente.html', {'form': form})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'my_app/listar_productos.html', {'productos': productos})


@login_required
@user_passes_test(is_admin)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'my_app/editar_producto.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('listar_productos')

def about(request):
    return render(request, 'my_app/about.html')
