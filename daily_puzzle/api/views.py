from rest_framework import generics
from my_django_project.daily_puzzle.models.models import DailyPuzzle
from my_django_project.daily_puzzle.serializer.serializers import DailyPuzzleSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку всіх ігор")
class DailyPuzzleList(generics.ListAPIView):
    queryset = DailyPuzzle.objects.all()
    serializer_class = DailyPuzzleSerializer


@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class DailyPuzzleRetrieve(generics.RetrieveAPIView):
    queryset = DailyPuzzle.objects.all()
    serializer_class = DailyPuzzleSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class DailyPuzzleCreate(generics.CreateAPIView):
    queryset = DailyPuzzle.objects.all()
    serializer_class = DailyPuzzleSerializer


@extend_schema(summary="оновлення даних про гру")
class DailyPuzzleUpdate(generics.UpdateAPIView):
    queryset = DailyPuzzle.objects.all()
    serializer_class = DailyPuzzleSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class DailyPuzzleDestroy(generics.DestroyAPIView):
    queryset = DailyPuzzle.objects.all()
    serializer_class = DailyPuzzleSerializer