# Generated by Django 5.0.4 on 2024-04-06 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_customer_usertype_deliveryboy_usertype_shop_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='registration',
        ),
    ]
