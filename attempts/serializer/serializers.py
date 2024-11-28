from rest_framework import serializers

from my_django_project.Puzzles.serializer.serializers import PuzzleMainSerializer
from my_django_project.attempts.models.models import Attempt
from my_django_project.solutions.serializer.serializers import SolutionMainSerializer
from my_django_project.user_stats.serializer.serializers import UserStatsMainSerializer


class AttemptSerializer(serializers.ModelSerializer):
    stats = UserStatsMainSerializer()
    solution = SolutionMainSerializer()
    puzzle = PuzzleMainSerializer()
    class Meta:
        model = Attempt
        fields = ['id', 'puzzle_id', 'user_id', 'attempt_text', 'is_successful', 'attempted_at', 'stats', 'solution','puzzle']