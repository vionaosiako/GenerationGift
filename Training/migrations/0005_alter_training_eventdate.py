# Generated by Django 4.0.6 on 2022-07-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Training', '0004_alter_training_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='eventdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
