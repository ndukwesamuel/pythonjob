# Generated by Django 3.1.1 on 2021-02-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0079_auto_20210216_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_detail',
            name='Company_logo',
            field=models.ImageField(default='images/profile1.png', null=True, upload_to='images/'),
        ),
    ]
