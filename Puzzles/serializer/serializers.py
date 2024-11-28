from rest_framework import serializers
from my_django_project.Puzzles.models.models import PuzzleMain
from my_django_project.attempts.serializer.serializers import AttemptSerializer
from my_django_project.daily_puzzle.serializer.serializers import DailyPuzzleSerializer
from my_django_project.hints.serializer.serializers import HintsMainSerializer
from my_django_project.puzzle_stats.serializer.serializers import PuzzleStatsMainSerializer


class PuzzleMainSerializer(serializers.ModelSerializer):
    attempt = AttemptSerializer()
    stats = PuzzleStatsMainSerializer()
    hints = HintsMainSerializer()
    deily = DailyPuzzleSerializer()
    class Meta:
        model = PuzzleMain
        fields = ['id','title','description','encoded_text','shift_value', 'attempt', 'stats', 'hints', 'deily']