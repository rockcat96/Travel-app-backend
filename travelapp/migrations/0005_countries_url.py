# Generated by Django 4.1.7 on 2023-02-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_countries_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]