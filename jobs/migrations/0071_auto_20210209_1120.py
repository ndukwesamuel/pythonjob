# Generated by Django 3.1.1 on 2021-02-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0070_auto_20210209_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_detail',
            name='Company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
