# Generated by Django 5.1.6 on 2025-03-01 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictive_maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='latitude',
            field=models.FloatField(default=28.7041),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='longitude',
            field=models.FloatField(default=77.1025),
        ),
    ]
