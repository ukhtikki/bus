# Generated by Django 5.1.5 on 2025-01-25 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_book_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='username',
        ),
    ]
