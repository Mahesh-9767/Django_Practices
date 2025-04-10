from django.db import models
# Create your views here.

class Koljobs(models.Model):
    company = models.CharField(max_length=50)
    date = models.DateField()
    email = models.CharField(max_length=50)
    elig = models.CharField(max_length=50)
    exp = models.IntegerField()
    add = models.CharField(max_length=80)
    skills = models.CharField(max_length=50)

class Bangjobs(models.Model):
    company = models.CharField(max_length=50)
    date = models.DateField()
    email = models.CharField(max_length=50)
    elig = models.CharField(max_length=50)
    exp = models.IntegerField()
    add = models.CharField(max_length=80)
    skills = models.CharField(max_length=50)

class Punejobs(models.Model):
    company = models.CharField(max_length=50)
    date = models.DateField()
    email = models.CharField(max_length=50)
    elig = models.CharField(max_length=50)
    exp = models.IntegerField()
    add = models.CharField(max_length=80)
    skills = models.CharField(max_length=50)
