# Generated by Django 3.1.1 on 2021-02-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_auto_20210202_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Company_logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
