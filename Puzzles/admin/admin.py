from django.contrib import admin
from my_django_project.Puzzles.models import PuzzleMain

@admin.register(PuzzleMain)
class PuzzleAdmin(admin.ModelAdmin):
    pass