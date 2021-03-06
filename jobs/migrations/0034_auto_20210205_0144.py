# Generated by Django 3.1.1 on 2021-02-05 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0033_auto_20210203_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='company_detail',
            name='Application_target',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='company_detail',
            name='How_to_apply',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company_detail',
            name='Job',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('intenship', 'intenship'), ('part-time', 'part-time'), ('Freelance', 'Freelance'), ('Temporary', 'Temporary')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company_detail',
            name='Job_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company_detail',
            name='Job_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company_detail',
            name='Level_of_seniority',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Junior', 'Junior'), ('Mid level', 'Mid level'), ('Senior', 'Senior'), ('Lead', 'Lead'), ('Manager', 'Manager')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company_detail',
            name='Location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company_detail',
            name='tags',
            field=models.ManyToManyField(to='jobs.Tag'),
        ),
        migrations.DeleteModel(
            name='Company_Creat_Job',
        ),
    ]
