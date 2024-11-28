from django.contrib import admin
from my_django_project.User.models import UserMain

@admin.register(UserMain)
class UserMainAdmin(admin.ModelAdmin):
    pass