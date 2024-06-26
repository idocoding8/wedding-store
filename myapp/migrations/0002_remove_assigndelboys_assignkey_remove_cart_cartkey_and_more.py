# Generated by Django 5.0.4 on 2024-04-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigndelboys',
            name='assignkey',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cartkey',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='compkey',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='ckey',
        ),
        migrations.RemoveField(
            model_name='deliveryboy',
            name='delkey',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='feedkey',
        ),
        migrations.RemoveField(
            model_name='login',
            name='lkey',
        ),
        migrations.RemoveField(
            model_name='login',
            name='status',
        ),
        migrations.RemoveField(
            model_name='login',
            name='usertype',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='offkey',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='pykey',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productkey',
        ),
        migrations.RemoveField(
            model_name='productreturn',
            name='returnkey',
        ),
        migrations.RemoveField(
            model_name='rentdtl',
            name='rentkey',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='eventkey',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliveryboy',
            name='email',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliveryboy',
            name='password',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='email',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='password',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
