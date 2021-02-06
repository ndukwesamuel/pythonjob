# Generated by Django 3.1.1 on 2021-02-06 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0040_auto_20210206_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(default=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=100),
        ),
    ]
