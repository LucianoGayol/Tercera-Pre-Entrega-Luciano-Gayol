"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import (listar_proveedores, crear_proveedor, editar_proveedor, borrar_proveedor,proveedor_detail, buscar_producto, cliente_detail, about, borrar_producto, editar_producto, inicio, crear_cliente, crear_producto, crear_compra, buscar_cliente, listar_clientes, editar_cliente, borrar_cliente, listar_productos)

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('clientes/detalle/<int:cliente_id>/', cliente_detail, name='cliente_detail'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('productos/', listar_productos, name='listar_productos'),
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
    path('productos/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('productos/borrar/<int:producto_id>/', borrar_producto, name='borrar_producto'),
    path('crear_compra/', crear_compra, name='crear_compra'),
    path('buscar_cliente/', buscar_cliente, name='buscar_cliente'),
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('clientes/borrar/<int:cliente_id>/', borrar_cliente, name='borrar_cliente'),
    path('about/', about, name='about'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/crear/', crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:proveedor_id>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/borrar/<int:proveedor_id>/', borrar_proveedor, name='borrar_proveedor'),
    path('proveedores/detalle/<int:proveedor_id>/', proveedor_detail, name='proveedor_detail'),
]
