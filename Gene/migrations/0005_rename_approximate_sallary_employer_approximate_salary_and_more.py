# Generated by Django 4.0.6 on 2022-07-07 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gene', '0004_employer_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='approximate_sallary',
            new_name='approximate_salary',
        ),
        migrations.AddField(
            model_name='employer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employer',
            name='category',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]