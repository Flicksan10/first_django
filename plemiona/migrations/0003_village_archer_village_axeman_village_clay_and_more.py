# Generated by Django 4.2.7 on 2023-11-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plemiona', '0002_village_user_alter_village_barracks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='archer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='village',
            name='axeman',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='village',
            name='clay',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='village',
            name='clay_pit',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='village',
            name='farm',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='village',
            name='granary',
            field=models.IntegerField(default=5000),
        ),
        migrations.AddField(
            model_name='village',
            name='iron',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='village',
            name='iron_mine',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='village',
            name='sawmill',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='village',
            name='wood',
            field=models.IntegerField(default=1000),
        ),
    ]
