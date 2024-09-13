# Generated by Django 5.1.1 on 2024-09-10 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('bonus', models.FloatField()),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.department')),
            ],
        ),
    ]
