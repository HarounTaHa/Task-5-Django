# Generated by Django 4.0.4 on 2022-04-20 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0002_alter_order_order_number_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shope.item'),
        ),
    ]