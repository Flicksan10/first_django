from django.db import models, IntegrityError
from django.conf import settings
import random

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

