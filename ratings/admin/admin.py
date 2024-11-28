from django.contrib import admin
from my_django_project.ratings.models import RatingMain

@admin.register(RatingMain)
class RatingMainAdmin(admin.ModelAdmin):
    pass