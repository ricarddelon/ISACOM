from django.contrib import admin

from apps.ventas_compras.ventas.models import Ventas, VentasDetalles
# Register your models here.

admin.site.register(Ventas)
admin.site.register(VentasDetalles)
