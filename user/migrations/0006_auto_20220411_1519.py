# Generated by Django 3.2.8 on 2022-04-11 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_connectionmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ConnectionModel',
            old_name='date_creagted',
            new_name='created_at'
        )
    ]
