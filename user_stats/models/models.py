from django.db import models

class UserStatsMain(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    total_attempts = models.IntegerField()
    successful_attempts = models.IntegerField()
    total_puzzles_solved = models.IntegerField()