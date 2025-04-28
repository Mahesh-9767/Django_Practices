# cookiapp/views.py
from django.shortcuts import render
from .forms import NameForm
import datetime

def forms_date(request):
    form = NameForm()  # FIXED: form-form_name() → form = NameForm()
    return render(request, 'Testapp/Home.html', {'form': form})

def disp_name(request):
    name = request.GET.get('name', '')  # safer to use .get()
    response = render(request, 'Testapp/dname.html', {'name': name})
    response.set_cookie('name', name)
    return response

def res_disp(request):
    name = request.COOKIES.get('name', 'Guest')
    date = datetime.datetime.now()
    return render(request, 'Testapp/result.html', {'name': name, 'date': date})  # FIXED: missing return
