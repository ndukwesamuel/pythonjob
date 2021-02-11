# Generated by Django 3.1.1 on 2021-02-09 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0069_auto_20210209_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_detail',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='company_detail',
            name='short_des',
        ),
        migrations.RemoveField(
            model_name='company_detail',
            name='user',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='email_address',
        ),
        migrations.AlterField(
            model_name='company_detail',
            name='Company_logo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
