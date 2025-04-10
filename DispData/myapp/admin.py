from django.contrib import admin
from myapp.models import student9767
# Register your models here.

class student9767Admin(admin.ModelAdmin):
    list_display=('name','age','dob','add')
    
admin.site.register(student9767,student9767Admin)
    