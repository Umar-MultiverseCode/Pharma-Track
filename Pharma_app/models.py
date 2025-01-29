# models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # You can add other fields if needed (like email, etc.)

    def __str__(self):
        return self.username
