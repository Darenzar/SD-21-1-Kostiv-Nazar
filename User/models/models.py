from django.db import models

class UserMain(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

