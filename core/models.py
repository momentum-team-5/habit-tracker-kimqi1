from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Habit_detail(models.Model):
    name = models.CharField(max_length=255)
    goal_target = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')

class daily_Record(models.Model):
    entry = models.TextField()
    date = models.DateField()
    habit = models.ForeignKey(Habit_detail, on_delete=models.CASCADE, related_name="dailyRecords")