from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.user_login_view, name='login'),
    path('register/', views.user_registration_view, name='register'),
    path('logout/', views.user_logout_view, name='logout'),
]
