from django.urls import path
from my_django_project.puzzle_stats.api.views import PuzzleStatsList, PuzzleStatsRetrieve, PuzzleStatsCreate, PuzzleStatsUpdate, PuzzleStatsDestroy


urlpatterns = [
    path('v1/puzzle_stats/',PuzzleStatsList.as_view(), name='puzzle_stats-list'),
    path('v1/puzzle_stats/<int:pk>/', PuzzleStatsRetrieve.as_view(), name='puzzle_stats-detail'),
    path('v1/puzzle_stats/create/', PuzzleStatsCreate.as_view(), name='puzzle_stats-create'),
    path('v1/puzzle_stats/<int:pk>/update/',PuzzleStatsUpdate.as_view(), name='puzzle_stats-update'),
    path('v1/puzzle_stats/<int:pk>/delete/', PuzzleStatsDestroy.as_view(), name='puzzle_stats-destroy'),
]