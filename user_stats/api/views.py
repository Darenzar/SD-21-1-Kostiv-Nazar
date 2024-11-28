from rest_framework import generics
from my_django_project.user_stats.models.models import UserStatsMain
from my_django_project.user_stats.serializer.serializers import UserStatsMainSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку всіх ігор")
class UserStatsList(generics.ListAPIView):
    queryset = UserStatsMain.objects.all()
    serializer_class = UserStatsMainSerializer


@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class UserStatsRetrieve(generics.RetrieveAPIView):
    queryset = UserStatsMain.objects.all()
    serializer_class = UserStatsMainSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class UserStatsCreate(generics.CreateAPIView):
    queryset = UserStatsMain.objects.all()
    serializer_class = UserStatsMainSerializer


@extend_schema(summary="оновлення даних про гру")
class UserStatsUpdate(generics.UpdateAPIView):
    queryset = UserStatsMain.objects.all()
    serializer_class = UserStatsMainSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class UserStatsDestroy(generics.DestroyAPIView):
    queryset = UserStatsMain.objects.all()
    serializer_class = UserStatsMainSerializer