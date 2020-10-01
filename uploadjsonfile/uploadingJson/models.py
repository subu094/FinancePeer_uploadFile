from django.db import models
import uuid
# Create your models here.
# class Person(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     location = models.CharField(max_length=50, blank=True)

class JsonDatas(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=300)