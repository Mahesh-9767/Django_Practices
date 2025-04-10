from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def devil3(request):
    msg= "I am JavaScript"
    return HttpResponse(msg)