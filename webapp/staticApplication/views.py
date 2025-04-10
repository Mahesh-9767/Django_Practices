from django.shortcuts import render

# Create your views here.

def Movies(request):
    head='Movies'
    names='Tody is watch movies..'
    names1='KGF'
    names2='Sikandar'
    names3='Chaava'
    d={'head':head,'names':names,'names1':names1,'names2':names2,'names3':names3}
    return render(request,'Testapp/Sports.html',d)


def sports(request):
    head='sports'
    names='Tody is IPL match..'
    names1='RCB vs GT'
    names2='RCB vs CSK'
    names3='RCB vs MI'
    d={'head':head,'names':names,'names1':names1,'names2':names2,'names3':names3}
    return render(request,'Testapp/Sports.html',d)

def politics(request):
    head='Politics'
    names='PM'
    names1='Narenadr Modi'
    names2='Modi'
    names3='Lalu'
    d={'head':head,'names':names,'names1':names1,'names2':names2,'names3':names3}
    return render(request,'Testapp/Sports.html',d)
    