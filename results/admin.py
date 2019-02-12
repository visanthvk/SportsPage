from django.contrib import admin
from .models import Results

class ResultsAdmin(admin.ModelAdmin):
    search_fields = ['gender','sport','team1','team2','match_number']
    list_filter = ['gender','sport','match_number']
    list_display = ['gender','sport','match_number','team1','team2','winner']

admin.site.register(Results, ResultsAdmin)