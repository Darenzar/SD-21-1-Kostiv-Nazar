from django.urls import path
from my_django_project.user_stats.api.views import UserStatsList, UserStatsRetrieve, UserStatsCreate, UserStatsUpdate, UserStatsDestroy


urlpatterns = [
    path('v1/user_stats/',UserStatsList.as_view(), name='user_stats-list'),
    path('v1/user_stats/<int:pk>/', UserStatsRetrieve.as_view(), name='user_stats-detail'),
    path('v1/user_stats/create/', UserStatsCreate.as_view(), name='user_stats-create'),
    path('v1/user_stats/<int:pk>/update/',UserStatsUpdate.as_view(), name='user_stats-update'),
    path('v1/user_stats/<int:pk>/delete/', UserStatsDestroy.as_view(), name='user_stats-destroy'),
]