# Generated by Django 4.2 on 2025-01-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(default='Ваш уникальный логин', max_length=150, unique=True),
        ),
    ]
