from django.db import models

class Attempt(models.Model):
    puzzle_id = models.ForeignKey('Puzzles', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    attempt_text = models.TextField()
    is_successful = models.BooleanField(auto_created=False)
    attempted_at = models.DateTimeField()

    def __str__(self):
        return self.attempt_text