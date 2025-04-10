from django.shortcuts import render
import datetime
# Create your views here.

def UI(request):
    date=datetime.datetime.now()
    d={'date':date,'Name':"Mahesh",'ID':6913}
    return render(request,'testapp/Homes.html',d)


