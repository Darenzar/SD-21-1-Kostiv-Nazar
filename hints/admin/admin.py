from django.contrib import admin
from my_django_project.hints.models import HintsMain

@admin.register(HintsMain)
class HintsAdmin(admin.ModelAdmin):
    pass