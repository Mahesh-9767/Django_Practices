from django import forms

class Employee(forms.Form):
    ename=forms.CharField(max_length=20)
    eage=forms.IntegerField()
    esal=forms.FloatField()