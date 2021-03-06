# Generated by Django 3.1.1 on 2021-02-03 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0030_auto_20210202_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Creat_Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=100, null=True)),
                ('Job', models.CharField(choices=[('Full-time', 'Full-time'), ('intenship', 'intenship'), ('part-time', 'part-time'), ('Freelance', 'Freelance'), ('Temporary', 'Temporary')], max_length=100, null=True)),
                ('Level_of_seniority', models.CharField(choices=[('Beginner', 'Beginner'), ('Junior', 'Junior'), ('Mid level', 'Mid level'), ('Senior', 'Senior'), ('Lead', 'Lead'), ('Manager', 'Manager')], max_length=100, null=True)),
                ('Job_description', models.TextField(null=True)),
                ('How_to_apply', models.TextField()),
                ('Application_target', models.CharField(max_length=200, null=True)),
                ('Location', models.CharField(max_length=100, null=True)),
                ('company_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.company_detail')),
            ],
        ),
    ]
