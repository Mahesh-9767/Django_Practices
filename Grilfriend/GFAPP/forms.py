# cookiapp/forms.py
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=20)

class Ageform(forms.Form):
    age = forms.IntegerField()

class GFforms(forms.Form):
    GFname = forms.CharField(max_length=20)
