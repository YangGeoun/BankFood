from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    age = models.IntegerField()
    salary = models.FloatField()
    money = models.FloatField()
    gender = models.TextField()
    risk_taking = models.BooleanField()
    adress = models.TextField()
    mbti = models.CharField(max_length=10)
