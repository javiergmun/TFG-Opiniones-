# Generated by Django 3.1.4 on 2022-06-07 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0015_alter_cliente_imagen_alter_empresa_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='contrasena',
        ),
    ]
