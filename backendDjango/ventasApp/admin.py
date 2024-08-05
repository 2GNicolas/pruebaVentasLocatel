from django.contrib import admin
from .models import Cabeceraventas, Detalleventas

class DetalleventasInline(admin.TabularInline):
    model = Detalleventas
    extra = 1

class CabeceraventasAdmin(admin.ModelAdmin):
    list_display = ( 'fecha', 'cliente', 'totalventa')
    search_fields = ('consecutivo', 'cliente__nombre')
    list_filter = ('fecha', 'cliente')
    inlines = [DetalleventasInline]

admin.site.register(Cabeceraventas, CabeceraventasAdmin)
