# Generated by Django 2.2.4 on 2021-07-12 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servidores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servidor',
            name='estado',
        ),
    ]
