from django.contrib import admin
from django.db import models
from .models        import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(RubroProd)
admin.site.register(OrdenCompra)