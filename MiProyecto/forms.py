from django import forms
from .models import Pedido, PedidoItem

class PedidoItemForm(forms.Form):
    producto_id = forms.IntegerField(widget=forms.HiddenInput)
    cantidad = forms.IntegerField(min_value=1, initial=1)
    personalizacion = forms.CharField(required=False, max_length=255)

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'correo', 'telefono', 'direccion', 'notas']
