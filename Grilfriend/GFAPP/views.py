from django.shortcuts import render
from .forms import NameForm, Ageform, GFforms
import datetime

# 1. Show the Name Form
def forms_date(request):
    form = NameForm()
    return render(request, 'Testapp/Home.html', {'form': form})

# 2. After submitting Name, show Age Form
def disp_name(request):
    name = request.GET.get('name', '')
    response = render(request, 'Testapp/dname.html', {
        'name': name,
        'form': Ageform()  # Show age form on next page
    })
    response.set_cookie('name', name)
    return response

# 3. After submitting Age, show GF name form
def age(request):
    age = request.GET.get('age', '')
    name = request.COOKIES.get('name', 'Guest')  # 👈 this line defines name
    response = render(request, 'Testapp/age.html', {
        'age': age,
        'name': name,          # 👈 pass name to template
        'form': GFforms()
    })
    response.set_cookie('age', age)
    return response


# 4. After submitting GF name, go to final result
def GF_name(request):
    gfname = request.GET.get('GFname', '')  # 👈 Match the field name exactly
    name = request.COOKIES.get('name', 'Guest')
    response = render(request, 'Testapp/GF.html', {
        'gfname': gfname,
        'name': name
    })
    response.set_cookie('gfname', gfname)
    return response



# 5. Show Final Result Page
def res_disp(request):
    name = request.COOKIES.get('name', 'Guest')
    age = request.COOKIES.get('age', 'Unknown')
    gf = request.COOKIES.get('gfname', 'No GF')
    date = datetime.datetime.now()
    return render(request, 'Testapp/result.html', {
        'name': name,
        'age': age,
        'GF': gf,
        'date': date
    })
