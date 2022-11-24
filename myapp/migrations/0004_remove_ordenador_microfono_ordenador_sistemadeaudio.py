# Generated by Django 4.1.3 on 2022-11-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_ordenador_procesador_ordenador_proces'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenador',
            name='microfono',
        ),
        migrations.AddField(
            model_name='ordenador',
            name='sistemaDeAudio',
            field=models.CharField(default='microfono', max_length=100),
        ),
    ]