# Generated by Django 3.2.2 on 2021-11-22 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Imagen',
            new_name='imagen',
        ),
    ]
