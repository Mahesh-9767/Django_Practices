from django.shortcuts import render

# Create your views here.

def Disp(request):
    A='Apple'
    B='Ball'
    C='Cat'
    my_dict={'a':A,'b':B,'c':C}
    return render(request,'Testapp/Homes.html',my_dict)
