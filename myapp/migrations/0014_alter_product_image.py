# Generated by Django 5.0.4 on 2024-04-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='images/'),
        ),
    ]
