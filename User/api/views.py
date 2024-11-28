from rest_framework import generics
from my_django_project.User.models.models import UserMain
from my_django_project.User.serializer.serializers import UserMainSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="отримання списку всіх ігор")
class UserList(generics.ListAPIView):
    queryset = UserMain.objects.all()
    serializer_class = UserMainSerializer


@extend_schema(summary="отримання деталей про конкретну гру", description='виводить всі дані про конкретний продукт')
class UserRetrieve(generics.RetrieveAPIView):
    queryset = UserMain.objects.all()
    serializer_class = UserMainSerializer


@extend_schema(summary="створення нового об'єкту(гри)")
class UserCreate(generics.CreateAPIView):
    queryset = UserMain.objects.all()
    serializer_class = UserMainSerializer


@extend_schema(summary="оновлення даних про гру")
class UserUpdate(generics.UpdateAPIView):
    queryset = UserMain.objects.all()
    serializer_class = UserMainSerializer


@extend_schema(summary="видалення гри", description='видаляє гру зі списку')
class UserDestroy(generics.DestroyAPIView):
    queryset = UserMain.objects.all()
    serializer_class = UserMainSerializer