# Generated by Django 3.2.9 on 2021-12-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211129_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='disciplina',
            field=models.ManyToManyField(blank=True, null=True, to='app.Disciplina'),
        ),
    ]