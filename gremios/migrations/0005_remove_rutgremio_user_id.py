# Generated by Django 2.2.1 on 2019-06-25 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gremios', '0004_auto_20190622_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rutgremio',
            name='user_id',
        ),
    ]
