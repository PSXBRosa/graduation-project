# Generated by Django 3.2.9 on 2021-12-09 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211209_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='exlcuido',
            new_name='excluido',
        ),
    ]