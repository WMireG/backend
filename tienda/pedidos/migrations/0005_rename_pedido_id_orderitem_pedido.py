# Generated by Django 5.0.6 on 2024-06-25 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_alter_orderitem_options_alter_pedido_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='pedido_id',
            new_name='pedido',
        ),
    ]