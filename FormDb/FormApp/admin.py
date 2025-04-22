from django.contrib import admin
from FormApp.models import Emp_model
class Emp_Admin(admin.ModelAdmin):
    list_display=['id','ename','esal','eadd']
admin.site.register(Emp_model,Emp_Admin)
# Register your models here.
