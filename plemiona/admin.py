from django.contrib import admin

from .models import Village


class QuestionAdmin(admin.ModelAdmin):
    fields = ['village_name',
              'coordinate_x',
              'coordinate_y',
              'town_hall',
              'barracks',
              'pikemen',
              'archer',
              'axeman',
              'wood',
              'iron',
              'clay',
              'granary',
              'farm',
              'sawmill',
              'iron_mine',
              'clay_pit',


              ]

admin.site.register(Village, QuestionAdmin)