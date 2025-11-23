from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Pedido, PedidoItem
from .forms import PedidoForm, PedidoItemForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse

def menu(request):
    categorias = Categoria.objects.prefetch_related('productos').all()
    return render(request, 'pedidos/menu.html', {'categorias': categorias})

def crear_pedido(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        # datos del pedido
        pedido_form = PedidoForm(request.POST)
        items = []
        for key, value in request.POST.items():
            if key.startswith('producto_'):
                pid = int(key.split('_',1)[1])
                try:
                    cantidad = int(value)
                except:
                    cantidad = 0
                if cantidad > 0:
                    personal = request.POST.get(f'personal_{pid}','').strip()
                    items.append({'producto_id': pid, 'cantidad': cantidad, 'personalizacion': personal})
        if pedido_form.is_valid() and items:
            pedido = pedido_form.save()
            for it in items:
                prod = Producto.objects.get(pk=it['producto_id'])
                PedidoItem.objects.create(pedido=pedido, producto=prod, cantidad=it['cantidad'], personalizacion=it['personalizacion'])
            # Envío de confirmación simple por correo (console backend)
            send_mail(
                subject=f'Confirmación pedido #{pedido.id}',
                message=f'Tu pedido fue recibido. ID: {pedido.id}. Estado: Pendiente.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[pedido.correo],
            )
            return redirect(pedido.get_absolute_url())
        else:
            return render(request, 'pedidos/crear_pedido.html', {'productos':productos, 'pedido_form': pedido_form, 'error':'Selecciona al menos un producto y completa tus datos.'})
    else:
        pedido_form = PedidoForm()
    return render(request, 'pedidos/crear_pedido.html', {'productos':productos, 'pedido_form': pedido_form})

def pedido_detalle(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    return render(request, 'pedidos/pedido_detalle.html', {'pedido': pedido})

def marcar_listo(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    pedido.estado = 'L'
    pedido.save()
    # notificar al cliente
    send_mail(
        subject=f'Pedido #{pedido.id} listo',
        message=f'Tu pedido #{pedido.id} está listo para recoger/enviar.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[pedido.correo],
    )
    return redirect(pedido.get_absolute_url())
