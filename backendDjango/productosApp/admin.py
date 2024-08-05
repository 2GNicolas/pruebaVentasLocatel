from django.contrib import admin

# Register your models here.

from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'valorventa', 'isiva', 'porcentajeiva')