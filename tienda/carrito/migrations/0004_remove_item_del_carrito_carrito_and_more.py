# Generated by Django 5.0.6 on 2024-06-13 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0003_alter_carrito_de_compra_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_del_carrito',
            name='carrito',
        ),
        migrations.RemoveField(
            model_name='item_del_carrito',
            name='producto',
        ),
        migrations.DeleteModel(
            name='carrito_de_compra',
        ),
        migrations.DeleteModel(
            name='Item_del_carrito',
        ),
    ]
