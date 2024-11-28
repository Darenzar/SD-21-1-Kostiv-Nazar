from django.contrib import admin
from my_django_project.attempts.models.models import Attempt

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    pass
