from django.contrib import admin
from .models import *

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Inventario)
admin.site.register(Pedido)
admin.site.register(DetallePedido)