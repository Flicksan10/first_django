# Generated by Django 4.2.7 on 2023-12-07 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plemiona', '0014_messagethread_last_notification_receiver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('last_notification_receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_notification_receiver', to=settings.AUTH_USER_MODEL)),
                ('replier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Message',
            new_name='Topic_message',
        ),
        migrations.DeleteModel(
            name='MessageThread',
        ),
        migrations.AddField(
            model_name='answers_message',
            name='topic_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='plemiona.topic_message'),
        ),
    ]
