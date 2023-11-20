from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
# Create your models here.
from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    pass

class User(AbstractUser):
    username = models.CharField(max_length=30) 
    nickname = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField()
    salary = models.IntegerField(blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    gender = models.BooleanField()
    address = models.TextField(blank=True, null=True)
    USERNAME_FIELD = 'nickname'
    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


# class User(AbstractBaseUser):
#     username = models.CharField(max_length=30)
#     nickname = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     money = models.IntegerField(blank=True, null=True)
#     salary = models.IntegerField(blank=True, null=True)
#     # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
#     financial_products = models.TextField(blank=True, null=True)
#     USERNAME_FIELD = 'nickname'
#     # superuser fields
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)