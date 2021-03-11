# Generated by Django 3.1.1 on 2021-03-11 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0081_auto_20210216_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_detail',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_content', to=settings.AUTH_USER_MODEL),
        ),
    ]
