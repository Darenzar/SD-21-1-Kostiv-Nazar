from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.post_create_view, name='create'),
    path('<int:pk>/', views.post_detail_view, name='detail'),
    path('<int:pk>/update/', views.post_update_view, name='update'),
    path('<int:pk>/delete/', views.post_delete_view, name='delete'),
]
