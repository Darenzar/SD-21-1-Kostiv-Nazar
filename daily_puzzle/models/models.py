from django.db import models

class DailyPuzzle(models.Model):
    puzzle_id = models.ForeignKey('Puzzles', on_delete=models.CASCADE)
    date = models.DateField()