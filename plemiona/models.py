from django.db import models, IntegrityError
from django.conf import settings
import random

from django import forms


class Village(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    village_name = models.CharField(max_length=100, default='New Village')
    coordinate_x = models.IntegerField(default=1)
    coordinate_y = models.IntegerField(default=1)
    pikemen = models.IntegerField(default=0)
    halberdiers = models.IntegerField(default=0)
    archer = models.IntegerField(default=0)
    axeman = models.IntegerField(default=0)
    light_cavalry = models.IntegerField(default=0)
    archer_cavalry = models.IntegerField(default=0)
    heavy_cavalry = models.IntegerField(default=0)
    wood = models.IntegerField(default=1000)
    iron = models.IntegerField(default=1000)
    clay = models.IntegerField(default=1000)
    town_hall = models.IntegerField(default=1)
    barracks = models.IntegerField(default=0)
    granary = models.IntegerField(default=1)
    farm = models.IntegerField(default=1)
    sawmill = models.IntegerField(default=1)
    iron_mine = models.IntegerField(default=1)
    clay_pit = models.IntegerField(default=1)
    stable = models.IntegerField(default=0)
    workshop = models.IntegerField(default=0)
    forge = models.IntegerField(default=0)
    market = models.IntegerField(default=0)
    wall = models.IntegerField(default=0)
    cache = models.IntegerField(default=0)
    palace = models.IntegerField(default=0)
    population_total = models.IntegerField(default=0)
    population_buildings = models.IntegerField(default=0)
    population_army = models.IntegerField(default=0)

    #     raports = models.CharField(max_length=10000, default='New Village')




    def __str__(self):
        return self.village_name

    def save(self, *args, **kwargs):
        while True:
            try:
                super().save(*args, **kwargs)
                break  # Jeśli zapis się powiedzie, wyjdź z pętli
            except IntegrityError:
                self.coordinate_x = random.randint(1, 10)
                self.coordinate_y = random.randint(1, 10)
                # Kontynuuj pętlę, aby ponownie spróbować zapisać

    class Meta:
        unique_together = ('coordinate_x', 'coordinate_y')

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):              # __unicode__ on Python 2
#         return self.choice_text

class Reports(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(max_length=100)
    attacker = models.CharField(max_length=100)
    defender = models.CharField(max_length=100)
    village_attacker_name = models.CharField(max_length=100)
    village_defender_name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    village_attacker_coordinates_x = models.IntegerField()
    village_attacker_coordinates_y = models.IntegerField()
    village_defender_coordinates_x = models.IntegerField()
    village_defender_coordinates_y = models.IntegerField()
    details = models.CharField(max_length=1000)
    def __str__(self):
        return f"Report {self.id} by {self.user.username}"


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, default='New Message')
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    # Możesz dodać więcej pól, jeśli potrzebujesz

class MessageThread(models.Model):
    message = models.ForeignKey(Message, related_name='replies', on_delete=models.CASCADE)
    replier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    # Możesz dodać więcej pól, jeśli potrzebujesz


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Możesz dodać więcej pól, np. typ powiadomienia, jeśli planujesz różne rodzaje powiadomień

    def __str__(self):
        return f"Powiadomienie dla {self.user.username}"

