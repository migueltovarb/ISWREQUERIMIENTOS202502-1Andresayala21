from django.contrib import admin
from .models import Categoria, Producto, Pedido, PedidoItem

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_cliente', 'correo', 'estado', 'creado')
    inlines = [PedidoItemInline]
    actions = ['marcar_listo']

    def marcar_listo(self, request, queryset):
        queryset.update(estado='L')
    marcar_listo.short_description = "Marcar pedidos seleccionados como LISTOS"

admin.site.register(Categoria)
admin.site.register(Producto)
