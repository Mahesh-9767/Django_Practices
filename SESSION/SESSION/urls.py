"""
URL configuration for SESSION project.

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
from SESSAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.firt_view, name='name'),               # Home
    path('age/', views.age_view, name='age'),             # Takes name and goes to age
    path('gf/', views.GF_view, name='gf'),                # Takes age and goes to gf
    path('res/', views.res_view, name='res'),       # Takes gf name and shows result
]
