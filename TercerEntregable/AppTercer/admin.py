from django.contrib import admin
from .models        import Cliente, Proveedor, Producto, RubroProd, OrdenCompra

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(RubroProd)
admin.site.register(OrdenCompra)