from django.db import models

class PuzzleStatsMain(models.Model):
    puzzle_id = models.ForeignKey('Puzzles', on_delete=models.CASCADE)
    average_rating = models.FloatField()
    total_attempts = models.IntegerField()
    successful_attempts = models.IntegerField()