# Generated by Django 2.2 on 2020-10-08 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20201008_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saledetail',
            old_name='date',
            new_name='sale',
        ),
    ]
