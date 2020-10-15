from django.db import models

class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=30)
    director=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    rating=models.FloatField()

# Create your models here.
