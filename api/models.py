from django.db import models

# Create your models here.

class PlayerStats(models.Model):
    player=models.CharField(max_length=10)
    session=models.CharField(max_length=36)
    level=models.CharField(max_length=10)
    action=models.IntegerField()
    time=models.FloatField()
    state=models.TextField()
