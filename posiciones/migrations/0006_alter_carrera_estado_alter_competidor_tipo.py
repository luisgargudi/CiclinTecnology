# Generated by Django 4.2.7 on 2023-12-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posiciones', '0005_alter_competidor_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='estado',
            field=models.CharField(choices=[('1', 'finalizada'), ('0', 'Sin Correr')], max_length=15, verbose_name='Estado de la carrera'),
        ),
        migrations.AlterField(
            model_name='competidor',
            name='tipo',
            field=models.TextField(choices=[('6', 'AB-'), ('3', 'B+'), ('5', 'AB+'), ('7', 'O+'), ('8', 'O-'), ('4', 'B-'), ('1', 'A+'), ('2', 'A-')], verbose_name='Tipo de Sangre'),
        ),
    ]
