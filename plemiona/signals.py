from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Village
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_village_for_new_user(sender, instance, created, **kwargs):
    if created:
        Village.objects.create(user=instance)
