from django.contrib import admin
from my_django_project.daily_puzzle.models import DailyPuzzle

@admin.register(DailyPuzzle)
class DailyPuzzleAdmin(admin.ModelAdmin):
   pass