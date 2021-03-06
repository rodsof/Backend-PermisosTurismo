# Generated by Django 3.2.3 on 2021-05-23 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisosturismo', '0004_auto_20210523_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='permiso',
            name='fechaGeneracion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='email',
            field=models.EmailField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='extranjero',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='sexo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='telefono',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='fecha',
            field=models.DateField(),
        ),
    ]
