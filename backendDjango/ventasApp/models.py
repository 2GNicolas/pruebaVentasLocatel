from django.db import models
from clientesApp.models import Cliente
from productosApp.models import Producto

# Create your models here.

class Cabeceraventas(models.Model):
    consecutivo = models.AutoField(db_column='Consecutivo', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cliente = models.ForeignKey('clientesApp.Cliente', models.DO_NOTHING, db_column='Cliente')  # Field name made lowercase.
    totalventa = models.IntegerField(db_column='TotalVenta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CabeceraVentas'
    
    def __str__(self):
        return f"Venta {self.consecutivo} - {self.fecha}"


class Detalleventas(models.Model):
    detalleid = models.AutoField(db_column='DetalleID', primary_key=True)  # Field name made lowercase.
    ventaconsecutivo = models.ForeignKey(Cabeceraventas,models.DO_NOTHING, db_column='VentaConsecutivo', related_name='detalles')  # Field name made lowercase.
    productocodigo = models.ForeignKey('productosApp.Producto', models.DO_NOTHING, db_column='ProductoCodigo')  # Field name made lowercase.
    valorproducto = models.IntegerField(db_column='ValorProducto')  # Field name made lowercase.
    iva = models.IntegerField(db_column='IVA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetalleVentas'
    
    def __str__(self):
        return f"Detalle {self.ventaconsecutivo} - Producto {self.producto}"