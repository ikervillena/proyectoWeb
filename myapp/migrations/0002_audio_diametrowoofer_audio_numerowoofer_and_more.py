# Generated by Django 4.1.3 on 2022-11-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='diametroWoofer',
            field=models.FloatField(default=16),
        ),
        migrations.AddField(
            model_name='audio',
            name='numeroWoofer',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='ordenador',
            name='memoria',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ordenador',
            name='microfono',
            field=models.CharField(default='microfono', max_length=10),
        ),
        migrations.AddField(
            model_name='ordenador',
            name='procesador',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='telefono',
            name='acabado',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='telefono',
            name='capacidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='telefono',
            name='pantalla',
            field=models.FloatField(default=0),
        ),
    ]