# Generated by Django 5.0.4 on 2024-04-09 08:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_rentdtl_currentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=60, validators=[django.core.validators.MaxLengthValidator(60)]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contact',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 to 12-digit contact number.', regex='^[0-9]{10,12}$')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customername',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='address',
            field=models.CharField(max_length=60, validators=[django.core.validators.MaxLengthValidator(60)]),
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='city',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='contactno',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 to 12-digit contact number.', regex='^[0-9]{10,12}$')]),
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='delname',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='district',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='email',
            field=models.EmailField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='pincode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Please enter a valid 6-digit pincode.', regex='^[0-9]{6}$')]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=60, validators=[django.core.validators.MaxLengthValidator(60)]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='contact',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 to 12-digit contact number.', regex='^[0-9]{10,12}$')]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='dist',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='email',
            field=models.EmailField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='pincode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Please enter a valid 6-digit pincode.', regex='^[0-9]{6}$')]),
        ),
    ]
