from django.shortcuts import render, redirect
from FormApp.form import Employee
from django.contrib import messages

def Employee_Form(request):
    name = None
    submission = False
    if request.method == 'POST':
        form = Employee(request.POST)
        if form.is_valid():
            name = form.cleaned_data['ename']
            submission = True
            return render(request, 'Testapp/index.html', {'form': Employee(), 'name': name, 'submission': submission})
    else:
        form = Employee()
        
    return render(request, 'Testapp/index.html', {'form': form, 'name': name, 'submission': submission})
