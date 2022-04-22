# Generated by Django 4.0.4 on 2022-04-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
    ]
