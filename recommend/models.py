from django.db import models
# Create your models here.

class Data(models.Model):
    date = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)
    type3 = models.CharField(max_length=100)
    rank = models.FloatField()
    search_count = models.FloatField()
    link = models.CharField(max_length=100)