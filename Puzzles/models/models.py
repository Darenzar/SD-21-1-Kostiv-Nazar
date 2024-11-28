from django.db import models

class PuzzleMain(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    encoded_text = models.CharField(max_length=50)
    shift_value = models.IntegerField()