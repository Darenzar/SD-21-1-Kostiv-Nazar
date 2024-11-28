"""
URL configuration for my_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/', include('attempts.urls')),
    path('api/', include('daily_puzzle.urls')),
    path('api/', include('hints.urls')),
    path('api/', include('puzzle_stats.urls')),
    path('api/', include('Puzzles.urls')),
    path('api/', include('ratings.urls')),
    path('api/', include('solutions.urls')),
    path('api/', include('User.urls')),
    path('api/', include('user_stats.urls')),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]