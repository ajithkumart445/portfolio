# Generated by Django 5.0.2 on 2024-06-25 14:05

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_projectinfo_image1_alter_projectinfo_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.GetFileName),
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.GetFileName),
        ),
    ]