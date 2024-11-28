from django.contrib import admin
from my_django_project.puzzle_stats.models import PuzzleStatsMain

@admin.register(PuzzleStatsMain)
class PuzzleStatsMainAdmin(admin.ModelAdmin):
    pass