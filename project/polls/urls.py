
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.create_question, name='create_question'),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/update/", views.update, name="update"),
    path('<int:question_id>/delete/', views.delete_question, name='delete_question'),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]