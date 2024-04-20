# Generated by Django 5.0.4 on 2024-04-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_customer_email_alter_deliveryboy_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='usertype',
            field=models.CharField(default='customer', max_length=100),
        ),
        migrations.AddField(
            model_name='deliveryboy',
            name='usertype',
            field=models.CharField(default='deliveryboy', max_length=100),
        ),
        migrations.AddField(
            model_name='shop',
            name='usertype',
            field=models.CharField(default='shop', max_length=100),
        ),
    ]
