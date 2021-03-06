# Generated by Django 3.2.8 on 2022-03-16 09:17

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'blank': 'このフィールドの入力は必須です', 'unique': 'あなたが入力したメールアドレスは既に使用されています。'}, max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'blank': 'このフィールドの入力は必須です'}, max_length=24, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
