from django.db import models

# Create your models here.


class Cliente(models.Model):
    cedula = models.CharField(db_column='Cedula', primary_key=True, max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'
        
    def __str__(self):
        return self.cedula