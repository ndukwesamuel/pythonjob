# Generated by Django 3.1.1 on 2021-02-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0052_auto_20210206_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_detail',
            name='Company_name',
            field=models.CharField(default='developer', max_length=100, null=True),
        ),
    ]
