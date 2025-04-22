from django.shortcuts import render
from .models import Emp_model

def employee_details(request):
    form=emp_form()
    if request.method=='POST':
        form=emp_form(request.POST)
        if form.save(commit=True)
        name=form.cleaned_data['ename']
        messages.success(request,f'{name} your form is filled')
    employees = Emp_model.objects.all()
    return render(request, 'index.html', {'employees': employees})

