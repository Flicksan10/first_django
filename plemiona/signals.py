from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Village, MessageThread, Notification
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_village_for_new_user(sender, instance, created, **kwargs):
    if created:
        Village.objects.create(user=instance)


@receiver(post_save, sender=MessageThread)
def create_notification_on_reply(sender, instance, created, **kwargs):
    if created:
        # Determine who should receive the notification
        recipient = instance.message.receiver if instance.replier == instance.message.sender else instance.message.sender

        Notification.objects.create(
            user=recipient,  # The user who will receive the notification
            message=instance.message,
            is_read=False
        )

        # Update the last_notification_receiver field in the MessageThread model
        instance.last_notification_receiver = recipient
        instance.save()