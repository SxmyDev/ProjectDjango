from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos relacionados con el producto, como categoría, cantidad en stock, etc.

    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    # Otros campos relacionados con el proveedor, como información de contacto adicional.

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    # Otros campos relacionados con el inventario, como ubicación, fecha de vencimiento, etc.

    def __str__(self):
        return f'{self.producto} - Cantidad: {self.cantidad}'

class Pedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetallePedido')
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=50)
    # Otros campos relacionados con el pedido, como número de orden, fecha de entrega estimada, etc.

    def __str__(self):
        return f'Pedido a {self.proveedor} - Número de Pedido: {self.id}'

class DetallePedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos relacionados con el detalle del pedido, como descuentos, subtotal, etc.

    def __str__(self):
        return f'Detalle de Pedido: {self.pedido.id}, Producto: {self.producto}'