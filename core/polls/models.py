import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):  # table
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):  # tasks
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=3000)

    def __str__(self):
        return self.choice_text


class Comment(models.Model):
    recipe = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comm')
    text = models.TextField()

    def __str__(self):
        return self.text
