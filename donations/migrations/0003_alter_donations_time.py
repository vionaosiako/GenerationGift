# Generated by Django 4.0.5 on 2022-07-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_donations_donation_date_donations_venue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]