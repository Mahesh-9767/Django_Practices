from django import forms
from FormApp.models import Emp_model
class Emp_form(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Emp_model