# Generated by Django 2.2.4 on 2020-03-27 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0014_auto_20200327_0751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previousorder',
            name='order_product',
        ),
        migrations.RemoveField(
            model_name='previousorder',
            name='order_user',
        ),
        migrations.DeleteModel(
            name='CancelOrder',
        ),
        migrations.DeleteModel(
            name='PreviousOrder',
        ),
    ]
