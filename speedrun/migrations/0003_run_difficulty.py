# Generated by Django 3.2 on 2021-05-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedrun', '0002_run_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='difficulty',
            field=models.CharField(choices=[('drizzle', 'Drizzle'), ('rainstorm', 'Rainstorm'), ('monsoon', 'Monsoon')], default='monsoon', max_length=30),
        ),
    ]