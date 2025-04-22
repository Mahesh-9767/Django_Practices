from django.contrib import admin
from movieapp.models import MovieMod
# Register your models here.
class AdminMov(admin.ModelAdmin):
    list_display=['id','mname','rdate','hero','heroine','director','lang','rating']
admin.site.register(MovieMod)   