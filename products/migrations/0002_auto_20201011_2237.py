# Generated by Django 2.2 on 2020-10-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod',
            name='price',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='prod',
            name='stok',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]
