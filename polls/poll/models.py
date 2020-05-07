from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    text = models.CharField(max_length=100, default=None, null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, default=None, null=True, on_delete=models.CASCADE)
    text = models.CharField(default=None, null=True, blank=True, max_length=100)
    votes = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.text