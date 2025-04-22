from django import forms
from .models import MovieMod
from .models import Contact

class Movie_Form(forms.ModelForm):
    class Meta:
        model = MovieMod
        fields = '__all__'
        
        
# movieapp/contact.py

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
