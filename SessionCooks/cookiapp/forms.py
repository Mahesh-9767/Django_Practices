# cookiapp/forms.py
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=20)
