from django.db import models

class Accounts(models.Model):
    """foodAccount model"""
    
    name = models.CharField(max_length=50)
    path_image = models.CharField(max_length=100)
    photo_habit = models.ImageField()
    photo_cheveux = models.ImageField()
    habits = models.CharField(max_length=100)
    coiffure = models.CharField(max_length=100)

