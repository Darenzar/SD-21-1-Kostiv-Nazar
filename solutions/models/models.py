from django.db import models

class SolutionMain(models.Model):
    puzzle_id = models.ForeignKey('Puzzles', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    solution_text = models.TextField()
    is_correct = models.BooleanField()
    attempted_at = models.DateTimeField()

