# Generated by Django 3.2.6 on 2021-08-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comany_name', models.CharField(max_length=100)),
                ('comany_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('salary', models.PositiveIntegerField()),
                ('prefectures', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
