# Generated by Django 2.2.4 on 2020-03-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0012_auto_20200327_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_city',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='order',
            name='order_pin',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='order',
            name='order_state',
            field=models.CharField(default=None, max_length=2000),
        ),
    ]
