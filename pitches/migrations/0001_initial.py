# Generated by Django 4.0.5 on 2022-07-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('mpesa_no', models.IntegerField()),
                ('decription', models.CharField(max_length=500)),
            ],
        ),
    ]