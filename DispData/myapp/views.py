from django.shortcuts import render
from myapp.models import student9767

# Create your views here.
def FetchData(request):
    data=student9767.objects.all()
    return render(request,'testapp/test.html',{'data':data})