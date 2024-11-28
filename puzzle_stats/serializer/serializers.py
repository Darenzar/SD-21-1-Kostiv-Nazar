from rest_framework import serializers

from my_django_project.Puzzles.serializer.serializers import PuzzleMainSerializer
from my_django_project.puzzle_stats.models.models import PuzzleStatsMain

class PuzzleStatsMainSerializer(serializers.ModelSerializer):
    puzzle = PuzzleMainSerializer()
    class Meta:
        model = PuzzleStatsMain
        fields =  ['puzzle_id', 'average_rating', 'total_attempts', 'successful_attempts','puzzle']