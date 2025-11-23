from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('pedido/nuevo/', views.crear_pedido, name='crear_pedido'),
    path('pedido/<int:id>/', views.pedido_detalle, name='pedido_detalle'),
    path('pedido/<int:id>/listo/', views.marcar_listo, name='pedido_listo'),
]
