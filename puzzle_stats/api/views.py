from rest_framework import generics
from my_django_project.puzzle_stats.models.models import PuzzleStatsMain
from my_django_project.puzzle_stats.serializer.serializers import PuzzleStatsMainSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку")
class PuzzleStatsList(generics.ListAPIView):
    queryset = PuzzleStatsMain.objects.all()
    serializer_class = PuzzleStatsMainSerializer


@extend_schema(summary="отримання деталей", description='виводить всі дані')
class PuzzleStatsRetrieve(generics.RetrieveAPIView):
    queryset = PuzzleStatsMain.objects.all()
    serializer_class = PuzzleStatsMainSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class PuzzleStatsCreate(generics.CreateAPIView):
    queryset = PuzzleStatsMain.objects.all()
    serializer_class = PuzzleStatsMainSerializer


@extend_schema(summary="оновлення даних про гру")
class PuzzleStatsUpdate(generics.UpdateAPIView):
    queryset = PuzzleStatsMain.objects.all()
    serializer_class = PuzzleStatsMainSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class PuzzleStatsDestroy(generics.DestroyAPIView):
    queryset = PuzzleStatsMain.objects.all()
    serializer_class = PuzzleStatsMainSerializer