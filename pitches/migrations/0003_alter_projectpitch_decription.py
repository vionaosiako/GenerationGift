# Generated by Django 4.0.5 on 2022-07-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0002_projectpitch_delete_pitch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpitch',
            name='decription',
            field=models.CharField(max_length=500),
        ),
    ]