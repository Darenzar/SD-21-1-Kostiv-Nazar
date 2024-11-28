from rest_framework import generics
from my_django_project.hints.models.models import HintsMain
from my_django_project.hints.serializer.serializers import HintsMainSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку всіх ігор")
class HintsList(generics.ListAPIView):
    queryset = HintsMain.objects.all()
    serializer_class = HintsMainSerializer


@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class HintsRetrieve(generics.RetrieveAPIView):
    queryset = HintsMain.objects.all()
    serializer_class = HintsMainSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class HintsCreate(generics.CreateAPIView):
    queryset = HintsMain.objects.all()
    serializer_class = HintsMainSerializer


@extend_schema(summary="оновлення даних про гру")
class HintsUpdate(generics.UpdateAPIView):
    queryset = HintsMain.objects.all()
    serializer_class = HintsMainSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class HintsDestroy(generics.DestroyAPIView):
    queryset = HintsMain.objects.all()
    serializer_class = HintsMainSerializer