from rest_framework import serializers
from my_django_project.ratings.models.models import RatingMain
from my_django_project.user_stats.serializer.serializers import UserStatsMainSerializer


class RatingMainSerializer(serializers.ModelSerializer):
    stats = UserStatsMainSerializer()
    class Meta:
        model = RatingMain
        fields = ['id', 'puzzle_id', 'user_id', 'rating_value','stats']
