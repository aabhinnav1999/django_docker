# Generated by Django 5.0.6 on 2024-06-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_cricket'),
    ]

    operations = [
        migrations.CreateModel(
            name='office',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=25)),
                ('salary', models.IntegerField()),
                ('reports_to', models.IntegerField()),
                ('office_id', models.IntegerField()),
            ],
        ),
    ]
