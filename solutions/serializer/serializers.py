from rest_framework import serializers

from my_django_project.attempts.serializer.serializers import AttemptSerializer
from my_django_project.solutions.models.models import SolutionMain

class SolutionMainSerializer(serializers.ModelSerializer):
    attempt = AttemptSerializer()
    class Meta:
        model = SolutionMain
        fields = ['id', 'user_id', 'puzzle_id', 'solution_text', 'is_correct', 'attempted_at','attempt']