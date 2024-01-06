from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Village, Answers_Message, Notification
from django.contrib.auth.models import User

@receiver(post_save, sender=Answers_Message)
def create_notification_on_reply(sender, instance, created, **kwargs):
    if created:
        # Determine who should receive the notification
        recipient = instance.topic_message.receiver if instance.replier == instance.topic_message.sender else instance.topic_message.sender

        Notification.objects.create(
            user=recipient,  # The user who will receive the notification
            message=instance.topic_message,
            is_read=False
        )

        # Update the last_notification_receiver field in the MessageThread model
        instance.last_notification_receiver = recipient
        instance.save()



# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_village_for_new_user(sender, instance, created, **kwargs):
#     if created:
#         Village.objects.create(user=instance)
