# Generated by Django 2.2 on 2020-10-08 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('phone', models.TextField(default='')),
                ('addrs', models.TextField(default='')),
                ('desc', models.TextField(default='')),
            ],
        ),
    ]
