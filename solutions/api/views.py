from rest_framework import generics
from my_django_project.solutions.models.models import SolutionMain
from my_django_project.solutions.serializer.serializers import SolutionMainSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку всіх ігор")
class SolutionsList(generics.ListAPIView):
    queryset = SolutionMain.objects.all()
    serializer_class = SolutionMainSerializer


@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class SolutionsRetrieve(generics.RetrieveAPIView):
    queryset = SolutionMain.objects.all()
    serializer_class = SolutionMainSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class SolutionsCreate(generics.CreateAPIView):
    queryset = SolutionMain.objects.all()
    serializer_class = SolutionMainSerializer


@extend_schema(summary="оновлення даних про гру")
class SolutionsUpdate(generics.UpdateAPIView):
    queryset = SolutionMain.objects.all()
    serializer_class = SolutionMainSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class SolutionsDestroy(generics.DestroyAPIView):
    queryset = SolutionMain.objects.all()
    serializer_class = SolutionMainSerializer