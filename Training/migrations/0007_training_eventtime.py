# Generated by Django 4.0.6 on 2022-07-05 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Training', '0006_alter_training_eventdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='eventtime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]