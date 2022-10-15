from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    fio = models.CharField(max_length=255,blank=True,null=True)
    email=models.EmailField()
    number=models.PositiveIntegerField(null=True,blank=True)
    birth_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("id",)
