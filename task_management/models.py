from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES , default="user")


class TaskModel(models.Model):
    STATUS_CHOICES = (
        ('complete', 'Complete'),
        ('pending', 'Pending'),
        ('inProcess', 'InProcess'),
    )
    name = models.CharField(max_length=225, blank=False,null=False)
    # assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=False,null=False, related_name='tasks')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} is {self.status}"

