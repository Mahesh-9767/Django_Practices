from django.shortcuts import render
from Back.models import *
# Create your views here.
def ma(request):
    return render(request,'Testapp/index.html')

def koljob(request):
    kj=Koljobs.objects.all()
    return render(request,'Testapp/kol.html',{'kj':kj})

def bangjob(request):
    bj=Bangjobs.objects.all()
    return render(request,'Testapp/bang.html',{'bj':bj})

def punejob(request):
    pj=Punejobs.objects.all()
    return render(request,'Testapp/pune.html',{'pj':pj})

