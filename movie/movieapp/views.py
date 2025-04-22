from django.shortcuts import render
from .models import MovieMod
from .forms import Movie_Form, ContactForm

# Create your views here.

def index_view(request):
    return render(request,'testapp/ind.html')


def list_movie(request):
    data=MovieMod.objects.all()
    return render(request,'testapp/movilist.html',{'data':data})


def adding_movie(request):
    form=Movie_Form()
    if request.method == 'POST':
        form=Movie_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
    
    return render(request,'testapp/addmov.html',{'form':form})

def parent(request):
    return render(request,'testapp/perent.html')



from .forms import ContactForm  # Make sure this is at the top
from django.shortcuts import redirect

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # redirect after successful submission
    return render(request, 'testapp/contact.html', {'form': form})

