# Generated by Django 5.0.2 on 2024-06-25 14:01

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.GetFileName),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
