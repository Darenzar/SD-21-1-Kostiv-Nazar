from django.urls import path
from my_django_project.ratings.api.views import RatingsList, RatingsRetrieve, RatingsCreate, RatingsUpdate, RatingsDestroy


urlpatterns = [
    path('v1/ratings/',RatingsList.as_view(), name='ratings-list'),
    path('v1/ratings/<int:pk>/', RatingsRetrieve.as_view(), name='ratings-detail'),
    path('v1/ratings/create/', RatingsCreate.as_view(), name='ratings-create'),
    path('v1/ratings/<int:pk>/update/',RatingsUpdate.as_view(), name='ratings-update'),
    path('v1/ratings/<int:pk>/delete/', RatingsDestroy.as_view(), name='ratings-destroy'),
]