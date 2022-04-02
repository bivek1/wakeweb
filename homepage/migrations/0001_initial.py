# Generated by Django 4.0.3 on 2022-04-02 14:45

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('short', models.CharField(max_length=300, unique=True)),
                ('aims', ckeditor_uploader.fields.RichTextUploadingField()),
                ('logo', models.ImageField(upload_to='logo/')),
            ],
        ),
    ]