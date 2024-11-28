from rest_framework import serializers
from my_django_project.User.models.models import UserMain
from my_django_project.user_stats.serializer.serializers import UserStatsMainSerializer


class UserMainSerializer(serializers.ModelSerializer):
    stats = UserStatsMainSerializer()

    class Meta:
        model = UserMain
        fields = ['id','user_name','email','password_hash','created_at','stats']
        # extra_kwargs = {
        #     'password_hash': {'write_only': True}  # Приховуємо поле паролю у відповіді API
        # }
