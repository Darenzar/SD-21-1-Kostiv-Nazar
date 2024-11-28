from django.urls import path
from my_django_project.Puzzles.api.views import PuzzlesList, PuzzlesRetrieve, PuzzlesCreate, PuzzlesUpdate, PuzzlesDestroy


urlpatterns = [
    path('v1/Puzzles/',PuzzlesList.as_view(), name='Puzzles-list'),
    path('v1/Puzzles/<int:pk>/', PuzzlesRetrieve.as_view(), name='Puzzles-detail'),
    path('v1/Puzzles/create/', PuzzlesCreate.as_view(), name='Puzzles-create'),
    path('v1/Puzzles/<int:pk>/update/',PuzzlesUpdate.as_view(), name='Puzzles-update'),
    path('v1/Puzzles/<int:pk>/delete/', PuzzlesDestroy.as_view(), name='Puzzles-destroy'),
]