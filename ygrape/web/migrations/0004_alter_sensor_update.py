# Generated by Django 3.2.9 on 2021-11-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_sensor_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='update',
            field=models.DateField(auto_now=True, verbose_name='update'),
        ),
    ]
