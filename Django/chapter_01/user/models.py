from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()
    hobby = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    career = models.CharField(max_length=50)

    def __str__(self):
        return self.name