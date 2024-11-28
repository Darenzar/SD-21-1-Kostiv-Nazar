from django.urls import path
from my_django_project.hints.api.views import HintsList, HintsRetrieve, HintsCreate, HintsUpdate, HintsDestroy


urlpatterns = [
    path('v1/hints/',HintsList.as_view(), name='hints-list'),
    path('v1/hints/<int:pk>/', HintsRetrieve.as_view(), name='hints-detail'),
    path('v1/hints/create/', HintsCreate.as_view(), name='hints-create'),
    path('v1/hints/<int:pk>/update/',HintsUpdate.as_view(), name='hints-update'),
    path('v1/hints/<int:pk>/delete/', HintsDestroy.as_view(), name='hints-destroy'),
]