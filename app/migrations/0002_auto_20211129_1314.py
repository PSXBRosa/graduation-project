# Generated by Django 3.2.9 on 2021-11-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='creditos_aula',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='creditos_trabalho',
            field=models.IntegerField(default=0),
        ),
    ]