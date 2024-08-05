from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(db_column='Codigo', primary_key=True, max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.     
    valorventa = models.IntegerField(db_column='valorVenta')  # Field name made lowercase.
    isiva = models.BooleanField(db_column='IsIVA')  # Field name made lowercase.
    porcentajeiva = models.IntegerField(db_column='PorcentajeIVA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'
    
    def __str__(self):
        return self.nombre