# Generated by Django 5.0.2 on 2024-07-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='challenges',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='results_learnings',
            field=models.TextField(),
        ),
    ]
