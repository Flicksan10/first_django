# Generated by Django 4.2.7 on 2023-12-04 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plemiona', '0007_reports_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='topic',
            field=models.CharField(default='Brak tematu', max_length=100),
        ),
    ]
