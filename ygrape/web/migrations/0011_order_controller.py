# Generated by Django 3.2.9 on 2021-11-22 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_trigger'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='controller',
            field=models.CharField(default=1, max_length=300, verbose_name='controller'),
            preserve_default=False,
        ),
    ]
