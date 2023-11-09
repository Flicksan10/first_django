from django.contrib import admin

from .models import Village


class QuestionAdmin(admin.ModelAdmin):
    fields = ['village_name', 'coordinate_x','coordinate_y','town_hall','barracks','pikemen','halberdiers']

admin.site.register(Village, QuestionAdmin)