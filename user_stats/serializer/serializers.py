from rest_framework import serializers

from my_django_project.User.serializer.serializers import UserMainSerializer
from my_django_project.attempts.serializer.serializers import AttemptSerializer
from my_django_project.ratings.serializer.serializers import RatingMainSerializer
from my_django_project.user_stats.models.models import UserStatsMain



class UserStatsMainSerializer(serializers.ModelSerializer):
    user = UserMainSerializer()
    rating = RatingMainSerializer()
    attempts = AttemptSerializer()
    class Meta:
        model = UserStatsMain
        fields = ['user_id','total_attempts','successful_attempts','total_puzzles_solved','user','rating','attempts']
