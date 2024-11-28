from django.urls import path
from my_django_project.User.api.views import UserList, UserRetrieve, UserCreate, UserUpdate, UserDestroy


urlpatterns = [
    path('v1/User/',UserList.as_view(), name='User-list'),
    path('v1/User/<int:pk>/', UserRetrieve.as_view(), name='User-detail'),
    path('v1/User/create/', UserCreate.as_view(), name='User-create'),
    path('v1/User/<int:pk>/update/',UserUpdate.as_view(), name='User-update'),
    path('v1/User/<int:pk>/delete/', UserDestroy.as_view(), name='User-destroy'),
]