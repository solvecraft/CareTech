# Generated by Django 5.0.4 on 2024-05-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('sn', models.CharField(max_length=20)),
                ('temperature', models.IntegerField()),
            ],
        ),
    ]
