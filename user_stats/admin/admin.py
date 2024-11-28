from django.contrib import admin
from my_django_project.user_stats.models import UserStatsMain

@admin.register(UserStatsMain)
class UserStatsMainAdmin(admin.ModelAdmin):
   pass