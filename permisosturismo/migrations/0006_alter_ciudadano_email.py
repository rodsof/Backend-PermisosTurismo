# Generated by Django 3.2.3 on 2021-05-23 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisosturismo', '0005_auto_20210523_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudadano',
            name='email',
            field=models.CharField(max_length=45, null=True),
        ),
    ]