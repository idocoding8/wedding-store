# Generated by Django 5.0.4 on 2024-04-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentdtl',
            name='currentdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
