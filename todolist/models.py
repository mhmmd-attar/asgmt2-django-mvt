from django.db import models

class Task(models.model):
    user = models.ForeignKey()
    date = models.DateField()
    title = models.CharField(max_length=64)
    description = models.TextField()