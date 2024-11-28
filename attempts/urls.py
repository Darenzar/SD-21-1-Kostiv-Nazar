from django.urls import path
from my_django_project.attempts.api.views import AttemptList, AttemptRetrieve, AttemptCreate, AttemptUpdate, AttemptDestroy


urlpatterns = [
    path('v1/attempts/', AttemptList.as_view(), name='attempts-list'),
    path('v1/attempts/<int:pk>/', AttemptRetrieve.as_view(), name='attempts-detail'),
    path('v1/attempts/create/', AttemptCreate.as_view(), name='attempts-create'),
    path('v1/attempts/<int:pk>/update/', AttemptUpdate.as_view(), name='attempts-update'),
    path('v1/attempts/<int:pk>/delete/', AttemptDestroy.as_view(), name='attempts-destroy'),
]