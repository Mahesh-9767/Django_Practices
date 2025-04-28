from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.

class HelloClass(View):
    def get(self, request):
        return HttpResponse('<h1>Hello, this response is from a class-based view</h1>')

class Tempapp_view(TemplateView):
    template_name = "Testapp/Home.html"  # Set the template name correctly

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'Rahul'
        context["age"] = 21
        context["sal"] = 100
        return context

# If you want another CBV for 'sec2/' path
class Tempapp_view2(TemplateView):
    template_name = "Testapp/Home2.html"  # You can use the same or a different template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'Vikaram'
        context["age"] = 22
        context["sal"] = 120
        return context
