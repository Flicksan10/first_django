# Generated by Django 4.2.7 on 2023-12-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plemiona', '0018_reports_date_created_alter_reports_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='loot',
            field=models.JSONField(default=dict),
        ),
    ]
