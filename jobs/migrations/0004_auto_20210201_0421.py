# Generated by Django 3.1.1 on 2021-02-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_company_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
