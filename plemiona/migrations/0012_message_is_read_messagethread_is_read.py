# Generated by Django 4.2.7 on 2023-12-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plemiona', '0011_remove_message_content_remove_message_reply_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='messagethread',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
