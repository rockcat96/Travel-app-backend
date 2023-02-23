from django.db import models

# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=100)
    cities = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    days = models.IntegerField(default=0)
    url = models.URLField(blank=True)
    
    
