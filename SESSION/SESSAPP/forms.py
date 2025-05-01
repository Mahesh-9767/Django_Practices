from django import forms

class Name_Form(forms.Form):
    name = forms.CharField(max_length=20)

class Age_form(forms.Form):
    age = forms.IntegerField()

class GF_forms(forms.Form):
    GFname = forms.CharField(max_length=20)
    
    
