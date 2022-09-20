from django.db import models
from django.core import validators as v

# Create your models here
class MyWatchList(models.Model):
    watched = models.CharField(max_length=1)
    title = models.CharField(max_length=64)
    rating = models.PositiveIntegerField(validators=[v.MinValueValidator(0), v.MaxValueValidator(10)], null=True)
    release_date = models.DateField()
    review = models.TextField()