# Generated by Django 4.2.7 on 2023-12-06 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plemiona', '0013_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagethread',
            name='last_notification_receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_notification_receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
