from django.shortcuts import render

# Create your views here.
def Home_view(request):
    return render(request,'Testapp/Home.html')


def Age_view(request):
    name=request.GET['name']
    resp=render(request,'Testapp/Age.html',{'name':name})
    resp.set_cookie('name',name)
    return resp

def GF_View(request):
    age=request.GET['age']
    name=request.COOKIES.get('name')
    resp=render(request,'Testapp/GF.html',{'name':name,'age':age})
    resp.set_cookie('age',age)
    return resp


def Res_view(request):
    gf=request.GET['gf']
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    resp=render(request,'Testapp/res.html',{'gf':gf,'name':name,'age':age})
    resp.set_cookie('gf',gf)
    return resp