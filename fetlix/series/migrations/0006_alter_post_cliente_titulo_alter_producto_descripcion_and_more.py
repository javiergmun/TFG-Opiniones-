# Generated by Django 4.0.4 on 2022-05-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_cliente',
            name='titulo',
            field=models.CharField(max_length=25, verbose_name='Titulo del post'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=300, verbose_name='Descripcion de producto en empresa'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='series/static/img/imagenes_producto', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=25, verbose_name='Nombre producto'),
        ),
    ]
