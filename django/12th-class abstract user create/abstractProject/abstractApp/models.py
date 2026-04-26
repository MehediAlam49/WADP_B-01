from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class custom_user(AbstractUser):
    USER=[
        ('admin','ADMIN'),
        ('simpleuser','Simpleuser')
    ]

    GENDER=[
        ('male','Male'),
        ('female','Female')
    ]

    userType=models.CharField(choices=USER,max_length=100)
    Gender=models.CharField(choices=GENDER, max_length=100)
    Address=models.CharField(max_length=100)
    Education=models.CharField(max_length=100)
