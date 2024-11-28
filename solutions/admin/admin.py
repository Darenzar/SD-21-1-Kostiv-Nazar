from django.contrib import admin
from my_django_project.solutions.models import SolutionMain

@admin.register(SolutionMain)
class SolutionMainAdmin(admin.ModelAdmin):
    pass