from django.contrib import admin
from Back.models import Punejobs,Koljobs,Bangjobs

# Register your models here.
class KolAdmin(admin.ModelAdmin):
    list_display=['company','date','email','elig','exp','add','skills']
    
admin.site.register(Koljobs,KolAdmin)


class BangAdmin(admin.ModelAdmin):
    list_display=['company','date','email','elig','exp','add','skills']
    
admin.site.register(Bangjobs,BangAdmin)


class PuneAdmin(admin.ModelAdmin):
    list_display=['company','date','email','elig','exp','add','skills']
    
admin.site.register(Punejobs,PuneAdmin)
