from django.urls import path
from my_django_project.solutions.api.views import SolutionsList, SolutionsRetrieve, SolutionsCreate, SolutionsUpdate, SolutionsDestroy


urlpatterns = [
    path('v1/solutions/',SolutionsList.as_view(), name='solutions-list'),
    path('v1/solutions/<int:pk>/', SolutionsRetrieve.as_view(), name='solutions-detail'),
    path('v1/solutions/create/', SolutionsCreate.as_view(), name='solutions-create'),
    path('v1/solutions/<int:pk>/update/',SolutionsUpdate.as_view(), name='solutions-update'),
    path('v1/solutions/<int:pk>/delete/', SolutionsDestroy.as_view(), name='solutions-destroy'),
]