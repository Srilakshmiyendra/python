from django.db import models

# Create your models here.
class register(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=20)
    Confirm_Password = models.CharField(max_length=20)