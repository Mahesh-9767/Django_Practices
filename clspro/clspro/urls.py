"""
URL configuration for clspro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cls/', views.HelloClass.as_view()),
    path('sec/', views.Tempapp_view.as_view()),
    path('sec2/', views.Tempapp_view2.as_view()),
    
]



