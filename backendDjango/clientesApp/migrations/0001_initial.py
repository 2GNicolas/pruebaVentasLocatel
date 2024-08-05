# Generated by Django 5.0.7 on 2024-08-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cedula', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Cedula', max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Nombre', max_length=50)),
                ('direccion', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Direccion', max_length=50)),
                ('telefono', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Telefono', max_length=50)),
                ('email', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Email', max_length=50)),
            ],
            options={
                'db_table': 'Cliente',
                'managed': False,
            },
        ),
    ]
