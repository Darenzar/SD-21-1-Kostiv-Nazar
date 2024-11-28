from rest_framework import serializers

from my_django_project.Puzzles.serializer.serializers import PuzzleMainSerializer
from my_django_project.daily_puzzle.models.models import DailyPuzzle

class DailyPuzzleSerializer(serializers.ModelSerializer):
    puzzle = PuzzleMainSerializer()

    class Meta:
        model = DailyPuzzle
        fields = ['id','puzzle_id', 'date','puzzle']

