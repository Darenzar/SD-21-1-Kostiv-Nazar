from django.db import models

class HintsMain(models.Model):
    puzzle_id = models.ForeignKey('Puzzles', on_delete=models.CASCADE)
    hint_text = models.TextField()
    hint_order = models.IntegerField()