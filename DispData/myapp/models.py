from django.db import models

# Create your models here.
# myapp/models.py
class student9767(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    dob = models.DateField()  # 👈 change from FloatField to DateField
    add = models.CharField(max_length=20)





