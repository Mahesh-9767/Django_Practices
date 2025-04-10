from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def devil2(request):
    msg= "I am A python"
    return HttpResponse(msg)
