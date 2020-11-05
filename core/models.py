from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class habit(models.Model):
    verb = models.CharField(max_length=20)
    noun = models.CharField(max_length=20)
    goal = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')

class record(models.Model):
    number = models.FloatField()
    is_met = models.BolleanField(default = False)
    date = models.DateField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="records")