from rest_framework import generics
from my_django_project.attempts.models.models import Attempt
from my_django_project.attempts.serializer.serializers import AttemptSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку всіх ігор")
class AttemptList(generics.ListAPIView):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer


@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class AttemptRetrieve(generics.RetrieveAPIView):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class AttemptCreate(generics.CreateAPIView):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer


@extend_schema(summary="оновлення даних про гру")
class AttemptUpdate(generics.UpdateAPIView):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class AttemptDestroy(generics.DestroyAPIView):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer