# Generated by Django 4.2.7 on 2023-11-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plemiona', '0003_village_archer_village_axeman_village_clay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='archer_cavalary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='village',
            name='heavy_cavalary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='village',
            name='light_cavalary',
            field=models.IntegerField(default=0),
        ),
    ]
