from django.shortcuts import render
from SESSAPP.forms import Name_Form,Age_form,GF_forms
# Create your views here.

# Create your views here.
def firt_view(request):
    form=Name_Form()
    return render(request,'Testapp/index.html',{'form':form})


def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    Age=Age_form()
    form=Name_Form()
    return render(request,'Testapp/age.html',{'form':form,'age':Age,'name':name})


def GF_view(request):
    age=request.GET['age']
    request.session['age']=age
    name=request.session['name']
    gf=GF_forms()
    return render(request,'Testapp/gf.html',{'age':age,'name':name,'gf':gf})


def res_view(request):
    GFname=request.GET['GFname']
    request.session['GFname']=GFname
    name=request.session['name']
    age=request.session['age']
    return render(request,'Testapp/res.html',{'GFname':GFname,'age':age,"name":name})

    

