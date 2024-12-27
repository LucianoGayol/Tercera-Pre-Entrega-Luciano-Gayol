from django import forms
from .models import Cliente, Producto, Compra, Proveedor, Message

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'body']
        # sender lo estableceremos en la vista (request.user)
