# Generated by Django 3.1.1 on 2021-02-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0076_auto_20210216_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='profile_pic',
            field=models.FileField(blank=True, default='media/profile1.png', null=True, upload_to='images/'),
        ),
    ]
