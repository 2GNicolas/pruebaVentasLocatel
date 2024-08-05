from django.contrib import admin

# Register your models here.


from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'direccion', 'telefono', 'email')