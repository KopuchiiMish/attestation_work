# Generated by Django 5.0.1 on 2024-01-29 23:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='chat_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='telegram_user_name',
        ),
    ]