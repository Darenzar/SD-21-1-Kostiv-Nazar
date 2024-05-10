from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path('<int:pk>/create/', views.create_comment_view, name='create'),
    path('<int:pk>/delete/', views.delete_comment_view, name='delete'),
]
