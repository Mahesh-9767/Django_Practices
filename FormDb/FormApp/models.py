from django.db import models


# Create your models here.
class Emp_model(models.Model):
    ename=models.CharField(max_length=20)
    eadd=models.CharField(max_length=30)
    esal=models.FloatField()