# Generated by Django 4.2.7 on 2023-12-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posiciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competidor',
            name='tipo',
            field=models.TextField(choices=[('3', 'B+'), ('8', 'O-'), ('7', 'O+'), ('4', 'B-'), ('1', 'A+'), ('6', 'AB-'), ('5', 'AB+'), ('2', 'A-')], verbose_name='Tipo de Sangre'),
        ),
    ]
