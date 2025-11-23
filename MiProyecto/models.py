from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"{self.nombre} - {self.precio}"

class Pedido(models.Model):
    ESTADOS = (
        ('P', 'Pendiente'),
        ('L', 'Listo'),
    )
    nombre_cliente = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
    notas = models.TextField(blank=True)

    def total(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Pedido #{self.id} - {self.nombre_cliente}"

    def get_absolute_url(self):
        return reverse('pedido_detalle', args=[self.id])

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    personalizacion = models.CharField(max_length=255, blank=True)

    def subtotal(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
