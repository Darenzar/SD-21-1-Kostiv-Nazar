from rest_framework import serializers

from my_django_project.Puzzles.serializer.serializers import PuzzleMainSerializer
from my_django_project.hints.models.models import HintsMain

class HintsMainSerializer(serializers.ModelSerializer):
    puzzle = PuzzleMainSerializer()
    class Meta:
        model = HintsMain
        fields = ['id','puzzle_id','hint_text','hint_order','puzzle']
