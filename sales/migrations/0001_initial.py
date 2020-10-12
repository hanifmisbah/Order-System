# Generated by Django 2.2 on 2020-10-11 15:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('qty', models.PositiveSmallIntegerField(default=0)),
                ('desc', models.TextField(default='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale', to=settings.AUTH_USER_MODEL)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terjual', to='products.Prod')),
            ],
        ),
    ]
