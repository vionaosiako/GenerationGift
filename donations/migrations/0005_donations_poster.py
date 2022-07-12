# Generated by Django 4.0.6 on 2022-07-12 17:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_rename_name_donations_donorname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='poster',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]