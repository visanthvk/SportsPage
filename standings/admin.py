from django.contrib import admin
from .models import Standings

class StandingsAdmin(admin.ModelAdmin):
    search_fields = ['gender','sport','team1','team2','team3']
    list_filter = ['gender','sport']
    list_display = ['gender','sport','team1','team2','team3']

admin.site.register(Standings, StandingsAdmin)