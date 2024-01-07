import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")
django.setup()

from django.contrib.auth.models import User
from plemiona.models import Research, ResearchTask  # Update with actual path

# Assuming you have a User model and each user should have one Research and one ResearchTask entry
for user in User.objects.all():
    village = user.village_set.first()  # Assuming a user has a village set

    # Create a Research entry for the user if not exists
    research, created = Research.objects.get_or_create(village=village)
    if created:
        print(f"Created Research for {user.username}")

    # Create a ResearchTask entry for the user if not exists
    # Update or create with default values for a new research task
    # research_task, created = ResearchTask.objects.get_or_create(
    #     village=village,
    # )
    if created:
        print(f"Created ResearchTask for {user.username}")
