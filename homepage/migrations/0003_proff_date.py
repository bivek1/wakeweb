# Generated by Django 4.0.3 on 2022-05-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_worker_proff'),
    ]

    operations = [
        migrations.AddField(
            model_name='proff',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]