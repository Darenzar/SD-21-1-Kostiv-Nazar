from django.urls import path
from my_django_project.daily_puzzle.api.views import DailyPuzzleList, DailyPuzzleRetrieve, DailyPuzzleCreate, DailyPuzzleUpdate, DailyPuzzleDestroy


urlpatterns = [
    path('v1/daily_puzzle/', DailyPuzzleList.as_view(), name='daily_puzzle-list'),
    path('v1/daily_puzzle/<int:pk>/', DailyPuzzleRetrieve.as_view(), name='daily_puzzle-detail'),
    path('v1/daily_puzzle/create/', DailyPuzzleCreate.as_view(), name='daily_puzzle-create'),
    path('v1/daily_puzzle/<int:pk>/update/', DailyPuzzleUpdate.as_view(), name='daily_puzzle-update'),
    path('v1/daily_puzzle/<int:pk>/delete/', DailyPuzzleDestroy.as_view(), name='daily_puzzle-destroy'),
]