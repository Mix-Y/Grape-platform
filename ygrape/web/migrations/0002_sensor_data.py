# Generated by Django 3.2.9 on 2021-11-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='data',
            field=models.CharField(default=0, max_length=20, verbose_name='data'),
            preserve_default=False,
        ),
    ]
