# Generated by Django 3.1.1 on 2021-02-08 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0060_auto_20210208_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_detail',
            name='user',
        ),
        migrations.DeleteModel(
            name='test',
        ),
        migrations.DeleteModel(
            name='test_detail',
        ),
    ]
