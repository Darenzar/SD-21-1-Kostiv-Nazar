from rest_framework import generics
from my_django_project.ratings.models.models import RatingMain
from my_django_project.ratings.serializer.serializers import RatingMainSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку всіх ігор")
class RatingsList(generics.ListAPIView):
    queryset = RatingMain.objects.all()
    serializer_class = RatingMainSerializer


@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class RatingsRetrieve(generics.RetrieveAPIView):
    queryset = RatingMain.objects.all()
    serializer_class = RatingMainSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class RatingsCreate(generics.CreateAPIView):
    queryset = RatingMain.objects.all()
    serializer_class = RatingMainSerializer


@extend_schema(summary="оновлення даних про гру")
class RatingsUpdate(generics.UpdateAPIView):
    queryset = RatingMain.objects.all()
    serializer_class = RatingMainSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class RatingsDestroy(generics.DestroyAPIView):
    queryset = RatingMain.objects.all()
    serializer_class = RatingMainSerializer