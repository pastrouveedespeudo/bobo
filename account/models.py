from django.db import models

class Accounts(models.Model):
    """foodAccount model"""
    
    name = models.CharField(max_length=50)
    photo = models.ImageField()
    habits = models.CharField(max_length=100)
    coiffure = models.CharField(max_length=100)
