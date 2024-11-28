from rest_framework import generics
from my_django_project.Puzzles.models.models import PuzzleMain
from my_django_project.Puzzles.serializer.serializers import PuzzleMainSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку всіх ігор")
class PuzzlesList(generics.ListAPIView):
    queryset = PuzzleMain.objects.all()
    serializer_class = PuzzleMainSerializer


@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class PuzzlesRetrieve(generics.RetrieveAPIView):
    queryset = PuzzleMain.objects.all()
    serializer_class = PuzzleMainSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class PuzzlesCreate(generics.CreateAPIView):
    queryset = PuzzleMain.objects.all()
    serializer_class = PuzzleMainSerializer


@extend_schema(summary="оновлення даних про гру")
class PuzzlesUpdate(generics.UpdateAPIView):
    queryset = PuzzleMain.objects.all()
    serializer_class = PuzzleMainSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class PuzzlesDestroy(generics.DestroyAPIView):
    queryset = PuzzleMain.objects.all()
    serializer_class = PuzzleMainSerializer