# Generated by Django 4.0.5 on 2022-07-01 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
                ('bio', models.TextField(blank=True, default='my bio', max_length=355)),
                ('name', models.CharField(blank=True, max_length=65)),
                ('email', models.EmailField(blank=True, max_length=120)),
                ('location', models.CharField(blank=True, max_length=65)),
                ('contact', models.CharField(blank=True, max_length=65)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
