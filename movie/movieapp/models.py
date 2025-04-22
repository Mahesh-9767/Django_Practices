from django.db import models

# Create your models here.


class MovieMod(models.Model):
    mname=models.CharField(max_length=20)
    rdate=models.DateField()
    hero=models.CharField(max_length=20)
    heroine=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    lang=models.CharField(max_length=20)
    rating=models.FloatField()



class Contact(models.Model):
    Name=models.CharField(max_length=20)
    Mob=models.IntegerField(max_length=10)
    Email=models.CharField(max_length=20)
    
    
    