from django.db import models, IntegrityError
from django.conf import settings
import random
from django.contrib.auth.models import User

from django import forms
from django.utils import timezone


class Village(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    village_name = models.CharField(max_length=100, default='New Village')
    coordinate_x = models.IntegerField(default=1)
    coordinate_y = models.IntegerField(default=1)
    town_hall = models.IntegerField(default=1)
    barracks = models.IntegerField(default=1)
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
    cache = models.IntegerField(default=1)
    palace = models.IntegerField(default=0)

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

class Army(models.Model):
    village = models.OneToOneField(Village, on_delete=models.CASCADE, related_name='army')
    pikemen_inside = models.IntegerField(default=0)
    pikemen_outside = models.IntegerField(default=0)
    halberdiers_inside = models.IntegerField(default=0)
    halberdiers_outside = models.IntegerField(default=0)
    archer_inside = models.IntegerField(default=0)
    archer_outside = models.IntegerField(default=0)
    axeman_inside = models.IntegerField(default=0)
    axeman_outside = models.IntegerField(default=0)
    light_cavalry_inside = models.IntegerField(default=0)
    light_cavalry_outside = models.IntegerField(default=0)
    archer_cavalry_inside = models.IntegerField(default=0)
    archer_cavalry_outside = models.IntegerField(default=0)
    heavy_cavalry_inside = models.IntegerField(default=0)
    heavy_cavalry_outside = models.IntegerField(default=0)


class ArmyHelp(models.Model):
    supporting_village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='sent_support')
    receiving_village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='received_support')
    pikemen = models.IntegerField(default=0)
    halberdiers = models.IntegerField(default=0)
    archer = models.IntegerField(default=0)
    axeman = models.IntegerField(default=0)
    light = models.IntegerField(default=0)
    archer_cavalry = models.IntegerField(default=0)
    heavy_cavalry = models.IntegerField(default=0)

class VillageResources(models.Model):
    village = models.OneToOneField('Village', on_delete=models.CASCADE, related_name='resources')
    wood = models.FloatField(default=1000)
    wood_bonus = models.FloatField(default=0)
    clay = models.FloatField(default=1000)
    clay_bonus = models.FloatField(default=0)
    iron = models.FloatField(default=1000)
    iron_bonus = models.FloatField(default=0)

    def __str__(self):
        return f"Resources for {self.village.village_name}"

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):              # __unicode__ on Python 2
#         return self.choice_text

class BuildingProperties(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='building_properties')
    building_type = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    performance = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    # Możesz dodać więcej dynamicznych pól, jeśli są potrzebne

    def __str__(self):
        return f"{self.building_type} properties for {self.village.village_name}"

    class Meta:
        unique_together = ('village', 'building_type')



class Reports(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(max_length=100)

    # Użytkownicy biorący udział w walce
    attacker_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='attacker_reports', on_delete=models.CASCADE)
    defender_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='defender_reports', on_delete=models.CASCADE)

    # Wioski biorące udział w walce
    village_attacker = models.ForeignKey(Village, related_name='attacker_village_reports', on_delete=models.CASCADE)
    village_defender = models.ForeignKey(Village, related_name='defender_village_reports', on_delete=models.CASCADE)

    # Armie i wynik
    attacker_army = models.JSONField(default=dict)
    defender_army = models.JSONField(default=dict)
    result = models.JSONField(default=dict)
    loot = models.JSONField(default=dict)

    # Zwycięzca
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='won_reports', on_delete=models.CASCADE, null=True, blank=True)
    loser = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='lost_reports', on_delete=models.CASCADE,
                              null=True, blank=True)

    details = models.CharField(max_length=1000, default="brak")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Report {self.id} by {self.attacker_user.username} vs {self.defender_user.username}"



class Topic_message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, default='New Message')
    date = models.DateTimeField(auto_now_add=True)
    is_readed_sender = models.BooleanField(default=True)
    is_readed_receiver = models.BooleanField(default=False)

    # Możesz dodać więcej pól, jeśli potrzebujesz

class Answers_Message(models.Model):
    topic_message = models.ForeignKey(Topic_message, related_name='replies', on_delete=models.CASCADE)
    replier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    last_notification_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_notification_receiver', null=True)
    # Możesz dodać więcej pól, jeśli potrzebujesz


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.ForeignKey(Topic_message, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Możesz dodać więcej pól, np. typ powiadomienia, jeśli planujesz różne rodzaje powiadomień

    def __str__(self):
        return f"Powiadomienie dla {self.user.username}"

class BuildingTask(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    building_type = models.CharField(max_length=100)
    target_level = models.IntegerField()
    completion_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Budowa {self.building_type} do poziomu {self.target_level} w {self.village.village_name} kończy się o {self.completion_time}"


class ArmyTask(models.Model):
    ACTION_CHOICES = [
        ('attack', 'Attack'),
        ('return_attack', 'Return from Attack'),
        ('defense_send', 'Send Defense'),
        ('defense_return', 'Return Defense'),
        # Dodaj więcej opcji według potrzeb
    ]

    attacker_village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='attacking_armies')
    defender_village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='defending_armies')
    army_composition = models.JSONField()  # Przechowuje skład armii
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES,default='attack')
    looted_resources = models.JSONField(default=dict)

class Research(models.Model):
    village = models.OneToOneField('Village', on_delete=models.CASCADE, related_name='research')
    pikemen = models.BooleanField(default=False)
    halberdiers = models.BooleanField(default=False)
    axeman = models.BooleanField(default=False)
    archer = models.BooleanField(default=False)
    light_cavalry = models.BooleanField(default=False)
    archer_cavalry = models.BooleanField(default=False)
    heavy_cavalry = models.BooleanField(default=False)
    catapult = models.BooleanField(default=False)
    ram = models.BooleanField(default=False)
    ballista = models.BooleanField(default=False)

class ResearchTask(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='research_tasks')
    research_type = models.CharField(max_length=100)  # np. 'pikemen', 'halberdiers', etc.
    completion_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Badanie {self.research_type} w {self.village.village_name} kończy się o {self.completion_time}"
