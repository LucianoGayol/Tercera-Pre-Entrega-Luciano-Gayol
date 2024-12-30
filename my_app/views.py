from django.shortcuts import render, redirect, get_object_or_404

from my_app.models import Cliente
from .forms import ClienteForm, ProductoForm, CompraForm, ProveedorForm, MessageForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto, Cliente, Compra, Proveedor, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



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


def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    compras_del_cliente = Compra.objects.filter(cliente=cliente)
    return render(request, 'my_app/cliente_detail.html', {
        'cliente': cliente,
        'compras': compras_del_cliente
    })

def buscar_producto(request):
    resultados = []
    query = request.GET.get('q', '')
    if query:
        # Busca productos cuyo nombre contenga 'query'
        resultados = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'my_app/buscar_producto.html', {
        'resultados': resultados,
        'query': query
    })


def is_admin(user):
    return user.is_staff

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'my_app/listar_proveedores.html', {'proveedores': proveedores})

@login_required
@user_passes_test(is_admin)
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'my_app/crear_proveedor.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'my_app/editar_proveedor.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.delete()
    return redirect('listar_proveedores')

def proveedor_detail(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'my_app/proveedor_detail.html', {'proveedor': proveedor})


@login_required
def inbox(request):
    """
    Lista todos los mensajes recibidos por el usuario logueado.
    """
    user = request.user
    # Todos los mensajes recibidos
    messages_list = Message.objects.filter(receiver=user).order_by('-date')
    return render(request, 'my_app/inbox.html', {'messages_list': messages_list})

@login_required
def outbox(request):
    """
    Lista todos los mensajes enviados por el usuario logueado.
    """
    user = request.user
    # Todos los mensajes enviados
    messages_list = Message.objects.filter(sender=user).order_by('-date')
    return render(request, 'my_app/outbox.html', {'messages_list': messages_list})


@login_required
def new_message(request):
    """
    Crea un mensaje nuevo. El sender es el usuario logueado.
    """
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_msg = form.save(commit=False)
            new_msg.sender = request.user  # El usuario logueado es el sender
            new_msg.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'my_app/new_message.html', {'form': form})


@login_required
def message_detail(request, msg_id):
    """
    Ver el detalle de un mensaje. Solo el sender o receiver deberían verlo.
    """
    msg = get_object_or_404(Message, id=msg_id)
    # Asegurarnos de que el user logueado sea sender o receiver
    if msg.sender != request.user and msg.receiver != request.user:
        return redirect('inbox')  # o algún error 403/404

    return render(request, 'my_app/message_detail.html', {'message': msg})

def signup(request):
    """
    Vista para registrar un usuario a través de un formulario
    básico de Django (UserCreationForm).
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Crea el usuario en la base de datos
            # Opcional: loguear automáticamente tras registrarse
            login(request, user)
            return redirect('inicio')  # Redirige a la vista 'inicio'
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
