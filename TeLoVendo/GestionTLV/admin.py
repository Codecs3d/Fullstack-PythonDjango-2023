from django.contrib import admin
from .models import Pedido, Producto, Estado, Categoria, FormaPago, Detalle, InfoCliente

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'orden', 'fecha', 'estado', 'id_pago')
    list_filter = ('fecha',)
    search_fields = ('orden',)
    list_per_page = 10
admin.site.register(Pedido, PedidoAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'precio', 'stock', 'categoria', 'imagen', 'descripcion')
    list_filter = ('nombre', 'precio', )
    search_fields = ('sku', )
admin.site.register(Producto, ProductoAdmin)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo',)
admin.site.register(Estado, EstadoAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo', )
    list_filter = ('titulo', )
admin.site.register(Categoria, CategoriaAdmin)

class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo', )
    list_filter = ('titulo', )
admin.site.register(FormaPago, FormaPagoAdmin)

class DetalleAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'total', 'id_producto', 'id_pedido')

admin.site.register(Detalle, DetalleAdmin)


class InfoClienteAdmin(admin.ModelAdmin):
    list_display = ('telefono', 'calle', 'numero', 'comuna', 'region')

admin.site.register(InfoCliente, InfoClienteAdmin)